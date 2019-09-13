# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import io
import time
import tweepy
import colorama  # Colorama streaming verbosity.

from konlpy.constants import DATA_DIR, ALPHABET, make_dir
from konlpy.stream import BaseStreamer
from konlpy.utils import delete_links, delete_mentions, pprint


class CorpusListener(tweepy.StreamListener):
    def __init__(self, options, dirname, word_list):
        """CorpusListener is a tweepy listener to listen on filtered list of words.

        Args:
            options (object): argparser argument namespace
            dirname (str): string of directory
            word_list (list): list of words
        """

        # WARNING: This underlining keys and tokens
        # should not be shared or uploaded on any public code repository!
        self.consumer_key = options.consumer_key
        self.consumer_secret = options.consumer_secret
        self.access_token = options.access_token
        self.access_token_secret = options.access_token_secret

        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(self.auth)

        self.dirname = dirname
        self.words = word_list
        self.options = options

        self.limit = 0
        self.init_time = time.time()

        colorama.init()

    def on_status(self, status):
        tweet = status.text

        # Except potentially repetitive retweets
        def write_tweets_to_files(tweet):
            if self.options.remove_links:
                tweet = delete_links(tweet)
            if self.options.remove_mentions:
                tweet = delete_mentions(tweet)

            word_count = 0

            if not self.options.output_as_onefile:
                # counts how many targeting words included in one tweet.
                for word in self.words:
                    word_count += tweet.count(word)

            filename = "{}{}{}.{}".format(
                self.dirname,
                self.options.output_prefix,
                word_count,
                self.options.output_extension
            )

            n_word_file = io.open(filename, 'a', encoding='utf-8')
            n_word_file.write(tweet)
            n_word_file.write("\n")

            if self.options.verbose:
                for word in self.words:
                    tweet = (colorama.Fore.CYAN + word).join(tweet.split(word))
                    tweet = (word + colorama.Fore.RESET).join(tweet.split(word))
                pprint(word_count, tweet)

        if self.options.filter_retweets:
            if not "RT @" in tweet:
                write_tweets_to_files(tweet)
                self.limit += 1
                if (self.limit == self.options.tweet_limits) | (
                        (time.time() - self.init_time) >= self.options.time_limits):
                    return False

        else:
            write_tweets_to_files(tweet)
            self.limit += 1
            if self.limit == self.options.tweet_limits:
                return False

    def on_error(self, status_code):
        if status_code == 420:  # if connection failed
            return False


class TwitterStreamer(BaseStreamer):
    """Start streaming on Twitter with your api keys and tokens.

    Args:
        dirname (str): directory to save output files.
        word_list (list): list of words to be streamed.
        async (bool): if true, apply threading in tweepy layer.
    """

    def __init__(self, dirname=DATA_DIR, word_list=ALPHABET, is_async=True):
        super(TwitterStreamer, self).__init__(is_async=is_async)
        self.is_async = is_async

        parser = self.get_parser()
        parser.add_argument(
            '--consumer_key',
            help='consumer key',
        )
        parser.add_argument(
            '--consumer_secret',
            help='consumer secret',
        )
        parser.add_argument(
            '--access_token',
            help='access token',
        )
        parser.add_argument(
            '--access_token_secret',
            help='access token secret',
        )
        parser.add_argument(
            '--filter_retweets',
            help='do not save potentially repetitive retweets',
            action="store_true",
        )
        parser.add_argument(
            '--remove_links',
            help='remove links included into each tweet',
            action="store_true",
        )
        parser.add_argument(
            '--remove_mentions',
            help='remove mentions included into each tweet',
            action="store_true",
        )
        parser.add_argument(
            '--output_prefix',
            help='prefix of the output file',
            default='tweet',
            type=str
        )
        parser.add_argument(
            '--output_as_onefile',
            help='save output as onefile',
            action="store_true",
        )
        parser.add_argument(
            '--output_extension',
            help='extension of the output file',
            default='txt',
            type=str
        )
        parser.add_argument(
            '--tweet_limits',
            help='stop when this amount of tweets are collected',
            default=1000000,
            type=int
        )
        parser.add_argument(
            '--time_limits',
            help='stop when n secs elapsed',
            default=1000000,
            type=int
        )
        parser.add_argument(
            '--keyword_file',
            help='file that defines a keywords line by line',
            type=str
        )

        self.options, _ = parser.parse_known_args()

        # lazy requirement checking since argparse's required option blocks initialization.
        requirements = [self.options.consumer_key, self.options.consumer_secret,
                        self.options.access_token, self.options.access_token_secret]

        flag = None
        for requirement in requirements:
            if not requirement:
                flag = 1

        if flag is not None:
            pprint("You have to provide valid consumer key, consumer_secret, access_token, access_token_secret.")

        # Parse wordlist from custom argument
        self.dirname = dirname
        if self.options.keyword_file is not None:
            try:
                reader = open(self.options.keyword_file, mode='r+', encoding='utf-8')
            except UnicodeDecodeError:
                reader = open(self.options.keyword_file, mode='r+', encoding='cp949')
            self.word_list = reader.readlines()

        else:
            self.word_list = word_list

        self.is_async = is_async
        self.streamer = None

    def create_listener(self):
        make_dir(directory=self.dirname)  # generates default konlpy data directory
        listener = CorpusListener(self.options, self.dirname, self.word_list)
        api = listener.api

        self.streamer = tweepy.Stream(auth=api.auth, listener=listener)

    def job(self):
        # FIXME: argument named "async" cannot be used in python3.7
        try:
            self.streamer.filter(track=self.word_list, is_async=self.is_async)
        except ValueError:
            raise ValueError("Please provide decent access token, secret, consumer key and secret")


def main():
    app = TwitterStreamer(is_async=False)
    app.options.verbose = True
    app.show_options()
    app.create_listener()
    app.stream()


if __name__ == '__main__':
    main()
