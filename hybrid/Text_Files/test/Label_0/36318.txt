
import java.io.*;
import java.util.*;

class Main{
	public static void main(String[] args){
		solve();
	}
	public static void solve(){
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] a = new int[n];
		int[] score = new int[4001];
		for(int i=0;i<n;i++){
			String s = sc.next();
			int counter = 3;
			for(int j=0;j<s.length();j++){
				if(j==1){
					continue;
				}
				a[i] += (int)Math.pow(10,counter)*((int)s.charAt(j)-(int)'0');
				counter--;
			}
		}

		for(int i=0;i<n;i++){
			score[a[i]]++;
		}		

		int now = 0;
		for(int i=0;i<=4000;i++){
			if(score[i]!=0){
				int tmp = score[i] - 1 + 3 * now;
				now += score[i];
				score[i] = tmp; 
			}
		}

		for(int i=0;i<n;i++){
			System.out.println(score[a[i]]);
		}

	}
}

