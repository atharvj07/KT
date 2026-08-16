import java.util.*;
 
public class Main{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int A = sc.nextInt();
		int B = sc.nextInt();
		int sq = (int)Math.sqrt((double)N);
		if((A+B>N+1) || (A<sq && B<sq)) System.out.println(-1);
		//(単調増加列)+(単調減少列)で表現できる
		else if(A+B==N+1){
			for(int i=B;i<=N;++i) System.out.print(i+" ");
			for(int i=B-1;i>=1;--i) System.out.print(i+" ");
			System.out.println();
		}else{
			//長さBの単調減少列のブロックを作れるだけ作る。その時最長増加部分列は
			//tempAで表されるので、Aとの差分を左端に単調増加列として追加する
			int tempA = (N/B)+(N%B!=0? 1:0);
			int hidari = 0;
			while(tempA+hidari!=A){
				hidari++;
				if(hidari>N){ //条件を満たす数列を作るのは無理くぼ
					System.out.println(-1);
					return;
				}
				if((N-hidari)%B==0) tempA--;
			}
			
			int nowN = N-hidari;
			for(int i=1;i<=hidari;++i) System.out.print(i+" "); //左端の単調増加列
			for(int i=1;i<=nowN/B;i++){
				for(int j=i*B;j>(i-1)*B;j--){
					System.out.print((j+hidari)+" "); //単調減少列のブロック
				}
			}
			for(int j=nowN;j>B*(nowN/B);--j) System.out.print((j+hidari)+" "); //あまった奴
			System.out.println();
		}
		return;
	}
}