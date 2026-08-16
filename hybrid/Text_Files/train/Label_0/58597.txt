import java.util.ArrayList;
import java.util.Scanner;
import java.util.StringTokenizer;


public class Main {

	Scanner sc;
	
	int solve(ArrayList<Integer> cards){
		int ace=0;
		int point=0;
		for(int card:cards){
			point+=card>10?10:card;
			ace+=card==1?1:0;
		}
		for(;point<=11&&ace>0;--ace){
			point+=10;
		}
		return point<=21?point:0;
	}
	
	String ns(){
		return sc.nextLine();
	}
	
	void io(){
		sc=new Scanner(System.in);
		
		while(true){
			StringTokenizer tok=new StringTokenizer(ns());
			ArrayList<Integer> cards=new ArrayList<Integer>();
			while(tok.hasMoreTokens()){
				cards.add(Integer.parseInt(tok.nextToken()));
			}
			if(cards.size()==1&&cards.get(0)==0) break;
			System.out.println(solve(cards));
		}
		sc.close();
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new Main().io();
	}

}