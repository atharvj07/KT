import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Main{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		while(true) {
			int N=sc.nextInt();
			if(N==0) {
				System.exit(0);
			}
			ArrayList<Integer> taro=new ArrayList<Integer>();
			ArrayList<Integer> hanako=new ArrayList<Integer>();
			int[] aa=new int[2*N];
			for(int i=0; i<2*N; i++) {
				aa[i]=i+1;
			}
			for(int i=0; i<N; i++) {
				int tmp=sc.nextInt();
				aa[tmp-1]=0;
				taro.add(tmp);
			}
			int counter=0;
			for(int i=0; i<2*N; i++) {
				if(aa[i]>0) {
					hanako.add(aa[i]);
				}
			}
			/*for(int i=0; i<N; i++) {
				p(taro.get(i)+" ");
			}
			pl("");
			for(int i=0; i<N; i++) {
				p(hanako.get(i)+" ");
			}
			pl();*/
			Collections.sort(taro);
			Collections.sort(hanako);
			int now=0;
			boolean tarohana=false;
			while(taro.size()>0 && hanako.size()>0) {
				if(tarohana==false) {	//太郎の番
					if(now==0) {
						now=taro.get(0);
						taro.remove(0);
						tarohana=true;
					}
					else {
						for(int i=0; i<taro.size(); i++) {
							if(taro.get(i)>now) {
								now=taro.get(i);
								taro.remove(i);
								tarohana=true;
								break;
							}
							else if(taro.get(i)<=now &&i==taro.size()-1) {
								now=0;
								tarohana=true;
							}
						}
					}
				}
				if(taro.size()==0 || hanako.size()==0) {
					break;
				}
				if(tarohana==true) {
					if(now==0) {
						now=hanako.get(0);
						hanako.remove(0);
						tarohana=false;
					}
					else {
						for(int i=0; i<hanako.size(); i++) {
							if(hanako.get(i)>now) {
								now=hanako.get(i);
								hanako.remove(i);
								tarohana=false;
								break;
							}
							else if(hanako.get(i)<=now &&i==hanako.size()-1) {
								now=0;
								tarohana=false;
							}
						}
					}
				}
			}
			if(taro.size()==0) {
				pl(hanako.size());
				pl(0);
			}
			else {
				pl(0);
				pl(taro.size());
			}
		}
	}
	public static void pl(Object o) {
		System.out.println(o);
	}
	public static void pl() {
		System.out.println();
	}
	public static void p(Object o) {
		System.out.print(o);
	}
}
