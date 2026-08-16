import java.util.*;
import java.io.*;
public class Main{
	public static void main(String[] args) {
		Scanner scn=new Scanner(System.in);
		int N = scn.nextInt();
		String S = scn.next();
		int[] visited1 = new int[26];
		int[] visited2 = new int[26];
		int c1=0, c2=0, max=-1;
		for(int i=0;i<N;i++){
			char ch=S.charAt(i);
			if ( visited1[ch-'a'] == 0){
				c1++;
			}
			visited1[ch-'a']++;
			
		}
		for(int i=0;i<N;i++){
			char ch=S.charAt(i);
			visited1[ch-'a']--;
			if ( visited1[ch-'a'] == 0){
				c1--;
			}
			if ( visited2[ch-'a'] == 0){
				c2++;
			}
			visited2[ch-'a']++;
			max=Math.max(max, countSame(visited1, visited2));
		}
		System.out.println(max);
	}
	static int countSame(int[] visited1, int[] visited2){
		int rv= 0;
		for(int i=0;i<26;i++){
			if(visited1[i]!=0 && visited2[i]!=0)
				rv++;
		}
		return rv;
	}
}


//gxdqkzhyutjlpt fxocrylqjnmubi