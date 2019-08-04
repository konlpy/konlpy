# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from datetime import datetime, timedelta
from konlpy.stream import BaseStreamer
from konlpy.data import StringWriter

import requests
import time
import json
import colorama

from colorama import Style, Fore
from konlpy.utils import pprint


class GoogleTrendStreamer(BaseStreamer):
    """Google is a biggest website in the world.
    GoogleTrendStreamer helps to stream trends from past to future.
    """

    def __init__(self, markup='lxml', is_async=True):
        super(GoogleTrendStreamer, self).__init__(is_async=is_async)
        self.is_async = is_async

        parser = self.get_parser()
        parser.add_argument(
            '--init_date',
            help='initial post_id to start crawling',
            default=datetime.today().strftime("%Y%m%d")
        )
        parser.add_argument(
            '--final_date',
            help='final post_id to stop crawling',
            default=datetime.today().strftime("%Y%m%d")
        )
        parser.add_argument(
            '--timeout',
            help='crawling timeout per request',
            default=5,
            type=float
        )
        parser.add_argument(
            '--interval',
            help='crawling interval per request to prevent blocking',
            default=0.5,
            type=float
        )
        parser.add_argument(
            '--metadata_to_dict',
            help='return metadata into dictionary type',
            action='store_true',
        )
        parser.add_argument(
            '--filename',
            help="filename to be saved.",
            default="google_trend.txt"
        )

        self.options, _ = parser.parse_known_args()
        self._session = requests.Session()
        self._markup = markup
        self._trend_url = 'https://trends.google.com/trends/api/dailytrends'

    def request_trend(self, date):
        """Request google trend data

        Args:
            hl (str): predefined id of gallery
            geo (int): integer of post number
            ed  (str): Target datetime. Based on 'YYYYMMDD' format.

        Returns:
            response: response of requests
        """
        query = {"hl": "ko", "geo": "KR", 'ed': date}
        response = self._session.get(self._trend_url, params=query, timeout=self.options.timeout)
        return response

    def get_trend(self, date):
        try:
            # Site's anti-bot policy may block crawling & you can consider gentle crawling
            time.sleep(self.options.interval)
            response = self.request_trend(date)
            pprint(response.status_code)
            response.raise_for_status()
            trend = self.parse_trend(response.content)

            return trend

        except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectTimeout):
            # if timeout occurs, retry
            return self.get_trend(date)

        except requests.exceptions.HTTPError:
            return None

    def parse_trend(self, content):
        # Preprocessing
        def preprocess(text):
            text = text.decode('unicode_escape')
            # 첫줄이')]}\',와 같은 의미없는 문자가 들어있어서 제외
            text = text.split('\n')[1]
            text = self._convert_utf8_to_euckr(text)
            return text

        trenddata = json.loads(preprocess(content))
        trendlist, date = self._get_trendlist_of_date(trenddata)
        trendlist = [
            {'title': trend['title']['query'],
             'traffic': trend['formattedTraffic'],
             # 'article_list' : trend['articles'],
             'date': date
             } for trend in trendlist
        ]
        return trendlist

    def job(self):
        colorama.init()
        writer = StringWriter(self.options.filename)

        def summary(result):
            for content in result:
                if not self.options.metadata_to_dict:
                    if self.options.verbose:
                        pprint(Fore.CYAN + content['date'] + Fore.RESET)
                        pprint(Fore.CYAN + Style.DIM + content['title'] + Style.RESET_ALL + Fore.RESET)
                        pprint(Fore.CYAN + Style.DIM * 2 + content['traffic'] + Style.RESET_ALL + Fore.RESET)
                    writer.write("@date:" + content['date'])
                    writer.write("@title:" + content['title'])
                    writer.write("@traffic:" + content['traffic'])
                else:
                    output = '\t'.join([content['date'], content['title'], content['traffic']])
                    if self.options.verbose:
                        pprint(output)
                    writer.write(output)

        def get_date_range(start_date, end_date):
            start = datetime.strptime(start_date, '%Y%m%d')
            end = datetime.strptime(end_date, '%Y%m%d')
            date_range = [(end - timedelta(days=x)).strftime("%Y%m%d")
                          for x in range(0, (end - start).days + 1)]
            return date_range

        for date in get_date_range(self.options.init_date, self.options.final_date):
            result = self.get_trend(date)
            if result is not None:
                summary(result)

    @staticmethod
    def _convert_utf8_to_euckr(unicode_str):
        return unicode_str.encode('euc-kr', 'replace').decode('euc-kr')

    @staticmethod
    def _get_trendlist_of_date(trend_data, target_date='yyyymmdd'):
        trends_list = trend_data['default']['trendingSearchesDays']
        for trend in trends_list:
            if(trend['date'] == target_date):
                return trend['trendingSearches'], trend['date']

        if trends_list:
            return trends_list[0]['trendingSearches'], trends_list[0]['date']  # default, most recently
        return [], []


def main():
    app = GoogleTrendStreamer(is_async=False)
    app.options.verbose = True
    app.stream()


if __name__ == "__main__":
    main()
