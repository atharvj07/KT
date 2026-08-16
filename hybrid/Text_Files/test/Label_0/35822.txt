import java.util.Scanner;
import java.util.Vector;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.ArrayList;
import java.util.Comparator;


public class C{
	public static void main(String[] args){
		Scanner in = new Scanner(System.in);
		StringBuilder a = new StringBuilder().append(in.next());
		StringBuilder b = new StringBuilder().append(in.next());
		int sumb = 0;
		int bsize = b.length();
		int curSum = 0;
		for(int i = 0;i<bsize;++i){
			if(b.charAt(i) == '1') sumb++;
			if(a.charAt(i) == '1') curSum++;
		}
		int res = ((sumb + curSum) % 2 == 0 ? 1: 0);
		for(int i = bsize;i<a.length();++i){
			if(a.charAt(i-bsize) == '1') curSum--;
			if(a.charAt(i) == '1') curSum++;
			if((sumb + curSum) % 2 == 0) res++;
		}
		System.out.println(res);
	}
} 
