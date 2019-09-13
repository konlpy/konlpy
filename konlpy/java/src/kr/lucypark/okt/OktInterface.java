package kr.lucypark.okt;

import java.util.ArrayList;
import java.util.List;

import scala.collection.Seq;
import scala.collection.Iterator;
import scala.collection.JavaConverters;

import org.openkoreantext.processor.util.KoreanPos;
import org.openkoreantext.processor.OpenKoreanTextProcessorJava;
import org.openkoreantext.processor.tokenizer.KoreanTokenizer.KoreanToken;
import org.openkoreantext.processor.phrase_extractor.KoreanPhraseExtractor;

public class OktInterface {

    public List<String> tokenize(String string, Boolean norm, Boolean stem) {
        final CharSequence charSeq = (norm) ? OpenKoreanTextProcessorJava.normalize(string) : string;

        final Seq<KoreanToken> seqTokens = OpenKoreanTextProcessorJava.tokenize(charSeq);
        Iterator<KoreanToken> tokenized = seqTokens.iterator();

        List<String> list = new ArrayList<>();
        while (tokenized.hasNext()) {
            final KoreanToken token = tokenized.next();
            if ( token.pos() == KoreanPos.Space() ) continue;
            final String text = (stem && !token.stem().isEmpty() ) ? token.stem().get() : token.text();
            final String str = text + '/' + token.pos();
            list.add(str);
        }
        return list;
    }

    public CharSequence normalize(String string) {
        return OpenKoreanTextProcessorJava.normalize(string);
    }

    public List<CharSequence> phrases(String string) {
        final CharSequence charSeq = string;
        final Seq<KoreanToken> tokens = OpenKoreanTextProcessorJava.tokenize(charSeq);
        List<KoreanPhraseExtractor.KoreanPhrase> phrases = OpenKoreanTextProcessorJava.extractPhrases(tokens, false, false);

        List<CharSequence> list = new ArrayList<>();
        for (KoreanPhraseExtractor.KoreanPhrase phrase : phrases) {
            final CharSequence tmpCharSeq = phrase.text();
            list.add(tmpCharSeq);
        }
        return list;
    }

    public static void main(String[] args) throws Exception {
        OktInterface ti = new OktInterface();

        List<String> tokens = ti.tokenize("아버지가 방에 들어가신다.", false, false);
        for (String token : tokens) {
            System.out.println(token);
        }
        System.out.println();

        List<CharSequence> phrases = ti.phrases("아버지가 방에 들어가신다.");
        System.out.println(phrases);
    }
}
