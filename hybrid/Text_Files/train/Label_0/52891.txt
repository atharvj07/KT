//Volume0-0095
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

class Player implements Comparable<Player>{
	public int a,
	           v;
	Player(int a,int v){
		this.a = a;
		this.v = v;
	}

	public int compareTo(Player t){
		return this.a - t.a;
	}
}

public class Main {

	public static void main(String[] args){

		//declare
		ArrayList<Player> ar = new ArrayList<Player>();

		int Champion = 0,
			num      = Integer.MIN_VALUE;

		//input
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        while(n-- > 0){
        	ar.add(new Player(sc.nextInt(),sc.nextInt()));
        }
        //calculate
        Collections.sort(ar);

        for(Player p:ar){
           	if( p.v > num){
           		Champion = p.a;
           		num      = p.v;
       		}
        }
       	//output
        System.out.println(Champion+" "+num);
	}
}