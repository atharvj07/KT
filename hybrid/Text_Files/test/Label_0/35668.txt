// サイコロを指示に従って転がし、終了時のtopの数字を出力
import java.util.*;
public class Main{
    static Scanner kbd = new Scanner(System.in);
    public static void main(String[] args){
	while(kbd.hasNext()){
	    int n = kbd.nextInt();
	    if(n != 0) solve(n);
	}
    }

    static void solve(int n){
	DiceR dice = new DiceR();
	while(n>0){
	    String order = kbd.next();
	    dice.rollO(order);
	    n--;
	}
	System.out.println(dice.getTop());
    }
}

class DiceR{
    int[] dice;
    public DiceR(){
	dice = new int[]{1, 2, 3, 6, 5, 4};
	// top, north, west, bottom, south, east
	//  0     1     2      3       4     5
    }

    public void rollO(String order){
	if(order.equals("north")){
	    roll(dice, 1, 0, 4, 3);
	}
	else if(order.equals("south")){
	    roll(dice, 4, 0, 1, 3);
	}
	else if(order.equals("east")){
	    roll(dice, 5, 0, 2, 3);
	}
	else if(order.equals("west")){
	    roll(dice, 2, 0, 5, 3);
	}
    }

    private void roll(int[] dice, int a, int b, int c, int d){
	// 引数を左に一つずらす。
	int p = dice[a];
	dice[a] = dice[b];
	dice[b] = dice[c];
	dice[c] = dice[d];
	dice[d] = p;
    }

    public int getTop(){ return dice[0]; }
}