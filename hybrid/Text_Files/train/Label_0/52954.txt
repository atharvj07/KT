import java.util.ArrayList;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// nameテ」ツ?ィtimeテ」ツ?ョテ」ツδ?」ツδシテ」ツつソテ」ツつ津」ツつづ」ツ?、テ」ツつッテ」ツδゥテ」ツつケテ」ツつ津」ツ?、テ」ツ?湘」ツつ?
		Scanner sc = new Scanner(System.in);
		int n=0,m=0;
		int[] timen = new int[31]; // テ」ツ?敕」ツ?ョテヲツ卍づ・ツ按サ(テヲツキツサテ・ツュツ?テ」ツ?ォテ」ツ??」ツつ凝、ツコツコテヲツ閉ー
		
		while(sc.hasNext()){
			n = sc.nextInt();
			if(n==0) break;
			
			charactor[] chara = new charactor[n];
			
			// テ」ツδ?」ツδシテ」ツつソテ・ツ?・テ・ツ環?
			for(int i = 0;i<n;i++){
				chara[i] = new charactor(sc.next());
				m = sc.nextInt();
				for(int j = 0;j<m;j++){
					int t = sc.nextInt();
					chara[i].addTime(t);
					timen[t]++;
				}
			}
			
			int minpoint = chara[0].getPoint(n,timen);
			String minname = chara[0].name;
			
			// テ」ツ?禿」ツ?禿」ツ?凝」ツつ英ointティツィツ暗ァツョツ?
			for(int i = 1;i<n;i++){
				//System.out.println(chara[i].name + ": " +chara[i].getPoint(n, timen));
				if(chara[i].getPoint(n, timen)<minpoint){
					minpoint = chara[i].getPoint(n, timen);
					minname = chara[i].name;
				}else if(chara[i].getPoint(n, timen)==minpoint){
					minname = chara[i].name.compareToIgnoreCase(minname)<0 ? chara[i].name : minname;
				}
			}
			
			System.out.println(minpoint + " " + minname);
		
			for(int i = 0;i<timen.length;i++) timen[i] = 0;
		}
	}

}

class charactor{
	ArrayList<Integer> time = new ArrayList<Integer>();
	String name;
	public charactor(String name){
		this.name = name;
	}
	void addTime(int t){
		time.add((Integer)t);
	}
	int getPoint(int n,int[] timen){
		int point=0;
		//System.out.print(name + ": ");
		for(int timei:time){
			point += n - (timen[timei]-1);
			//System.out.print(point + " ");
		}
		//System.out.println("]");
		return point;
	}
}