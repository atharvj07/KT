import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc= new Scanner(System.in);
		int N=sc.nextInt();
		int player[][]=new int[N][3]; //ゲーム数,何人目
		int point[][]=new int[N][3];
		int result[]=new int[N];
		for(int i=0;i<N;i++){
			for(int j=0;j<3;j++){
				int input =sc.nextInt();
				player[i][j]=input;//書いた数を得点としておく
				point[i][j] = input;//書いた数を得点としておく
			}
		}
		for(int i=0;i<3;i++){//３回分
			for(int j=0;j<N;j++){//j人目を決定
				for(int k=j+1;k<N;k++){//j人目以降で同じ人を探す。
					if(player[j][i]==player[k][i]){
						point[j][i]=0;
						point[k][i]=0;
						break;
				}
				}
			}
		}
		for(int i=0;i<N;i++){//３回分のポイントを出力
			for(int j=0;j<3;j++){
				result[i]+=point[i][j];
			}
		}
		for(int i=0;i<N;i++){//Nこ出力
			System.out.println(result[i]);
		}
	}
}