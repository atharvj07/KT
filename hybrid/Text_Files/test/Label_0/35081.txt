import java.util.*;
public class tic_tac_toe {
	public static void main(String[] args){
		Scanner scan = new Scanner(System.in);
		String input;
		char[][] a = new char[4][4];
		for(int i=0;i<4;i++){
			input = scan.nextLine();
			for(int j=0;j<4;j++){
				a[i][j] = input.charAt(j);
			}
		}
		for(int i=0;i<4;i++){//行
			for(int j=0;j<2;j++){
				if(call(a[i][j],a[i][j+1],a[i][j+2])) result(1);
			}
		}
		for(int i=0;i<2;i++){
			for(int j=0;j<4;j++){ //列
				if(call(a[i][j],a[i+1][j],a[i+2][j])) result(1);
			}
			if(call(a[i][i],a[i+1][i+1],a[i+2][i+2])) result(1);   //主对角线
			if(call(a[i][3-i],a[i+1][2-i],a[i+2][1-i])) result(1);
		}
		//长度为3的四条对角线
		if(call(a[0][1],a[1][2],a[2][3])) result(1);
		if(call(a[1][0],a[2][1],a[3][2])) result(1);
		if(call(a[0][2],a[1][1],a[2][0])) result(1);
		if(call(a[1][3],a[2][2],a[3][1])) result(1);
		result(0);
	}
	public static boolean call(char a,char b,char c){
		if(a=='x'&&b=='x'&&c=='.') return true;
		if(a=='x'&&b=='.'&&c=='x') return true;
		if(a=='.'&&b=='x'&&c=='x') return true;
		return false;
	}
	public static void result(int win){
		if(win == 1) System.out.println("YES");
		else if(win == 0) System.out.println("NO");
		System.exit(0);
	}
}
	 	  	 	 	  		  			  				   		