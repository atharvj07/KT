import java.util.*;
import java.math.*;

public class mayn {

	public static void main(String[] args) {
		Scanner scan = new Scanner (System.in);
		String sentence = scan.nextLine();
		boolean yep = true;
		String[] words = sentence.split(" ");
		int wlen = words.length;
		int [] wordstype = new int [wlen];
		for (int i=0 ; i<wlen ; i++) {
			wordstype[i] = isPetyish(words[i]);
			//System.out.println(wordstype[i]);
			if (wordstype[i] == -1) {
				yep = false;
			}
		}
		if (!grammar(wordstype)) {
			yep = false;
		}
		//System.out.println(yep);
		if (yep) {
			System.out.println ("YES");
		} else {
			System.out.println ("NO");
		}
	}
	
	public static int isPetyish (String word) {
		String [] endings = {"lios","liala","etr","etra","initis","inites"};
		int check = -1;
		int len = word.length ();
		if (len < 3) {
			return check;
		} else {
			for (int i=0 ; i<6 ; i++) {
				if (atTheEnd(word,endings[i])) {
					check = i;
				}
			}
		}
		return check;
	}
	
	public static boolean atTheEnd (String text, String pattern) {
		int tlen = text.length();
		int plen = pattern.length();
		//System.out.println(text + " has come here");
		//System.out.println(pattern + " has come here");
		if (plen > tlen) {
			return false;
		}
		if (text.substring((tlen-plen) , tlen).equals(pattern)) {
			//System.out.println("oldu");
			return true;
		} else {
			return false;
		}
	}
	
	public static boolean grammar (int [] words) {
		boolean check = true;
		if ((words[0]%2) == 1) {
			for (int i=0 ; i<words.length ; i++) {
				words[i]--;
			}
		}
		int nouncount = 0;
		int types [] = {0,2,4};
		int ptr = 0;
		for (int i=0 ; i < words.length ; i++) {
			while ((ptr < 3) && (words[i] != types[ptr])) {
				ptr++;
				//System.out.println("annen");
			}
			if (ptr == 1) {
				nouncount++;
			}
		}
		if ((ptr > 2)||(nouncount != 1)) {
			check = false;
		}
		if ((words.length == 1) && (ptr < 3)){
			check = true;
		}
		return check;
	}
}