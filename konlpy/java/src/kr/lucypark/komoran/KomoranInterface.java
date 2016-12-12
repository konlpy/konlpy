package kr.lucypark.komoran;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

import kr.co.shineware.nlp.komoran.core.analyzer.Komoran;
import kr.co.shineware.util.common.model.Pair;

public class KomoranInterface {

	private Komoran komoran = null;

	private void initKomoran(String dicpath){
		if(komoran == null){
			komoran = new Komoran(dicpath);
		}
	}
	
    public List<ArrayList<String>> analyzeMorphs(String phrase, String dicpath) {
		initKomoran(dicpath);
		List<List<Pair<String,String>>> result = komoran.analyze(phrase);

        List<ArrayList<String>> list = new ArrayList<ArrayList<String>>();

        for (List<Pair<String, String>> eojeolResult : result) {
            ArrayList<String> sublist = new ArrayList<String>();
            for (Pair<String, String> wordMorph : eojeolResult) {
                String str = wordMorph.getFirst() + '/' + wordMorph.getSecond();
                sublist.add(str);
            }
            list.add(sublist);
        }
        return list;
    }

    public List<String> analyzeMorphs3(String phrase, String dicpath) {
		initKomoran(dicpath);
        List<List<Pair<String,String>>> result = komoran.analyze(phrase);

        List<String> list = new ArrayList<String>();

        for (List<Pair<String, String>> eojeolResult : result) {
            String sublist = new String();
            for (Pair<String, String> wordMorph : eojeolResult) {
                String str = wordMorph.getFirst() + '/' + wordMorph.getSecond();
                sublist += '+' + str;
            }
            list.add(sublist); }
        return list;
    }

    public static void main(String[] args) throws Exception {
        KomoranInterface ki = new KomoranInterface();

        long lStartTime = new Date().getTime();

        List<ArrayList<String>> result = ki.analyzeMorphs("아버지가 방에 들어가신다.", "/Users/e9t/dev/pkgs/java/komoran-2.4/models");
        for (List<String> eojeolResult : result) {
            for (String wordMorph : eojeolResult) {
                System.out.println(wordMorph);
            }
            System.out.println();
        }

        long lEndTime = new Date().getTime();
        long difference = lEndTime - lStartTime;

        System.out.println("Elapsed milliseconds: " + difference);
    }
}
