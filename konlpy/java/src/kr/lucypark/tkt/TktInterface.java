package kr.lucypark.tkt;

import java.util.ArrayList;
import java.util.List;

import kr.co.shineware.util.common.model.Pair;

import com.twitter.penguin.korean.TwitterKoreanProcessorJava;
import com.twitter.penguin.korean.tokenizer.KoreanTokenizer;

public class TktInterface {

    public List<String> parser(String string) {
        TwitterKoreanProcessorJava processor = new TwitterKoreanProcessorJava.Builder().build();
        List<KoreanTokenizer.KoreanToken> tokens = processor.tokenize(string);

        List<String> list = new ArrayList<>();
        for (KoreanTokenizer.KoreanToken token: tokens) {
        	String str = token.text() + '/' + token.pos();
        	list.add(str);
        }
        return list;
    }

    public static void main(String[] args) throws Exception {
        TktInterface ti = new TktInterface();

        List<String> result = ti.parser("아버지가 방에 들어가신다.");
        for (String word : result) {
            System.out.println(word);
        }
        System.out.println();
    }
}