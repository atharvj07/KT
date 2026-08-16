import java.util.Scanner;

//TETORIS
public class Main{

//	static void p(boolean[][] m){
//		System.out.println();
//		for(int i=10;i>=0;i--){
//			for(int j=0;j<5;j++){
//				System.out.print(m[i][j]?"1":"0");
//			}
//			System.out.println();
//		}
//	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while(true){
			int n = sc.nextInt();
			if(n==0)break;
			boolean[][] m = new boolean[5000][5];
			while(n--!=0){
				int d = sc.nextInt();
				int p = sc.nextInt();
				int q = sc.nextInt()-1;
				if(d==2){
					int k = 4999;
					while(k>=0&&!m[k][q])k--;
					k++;
					for(int i=k;i<k+p;i++)m[i][q]=true;
				}
				else{
					int k = 4999;
					while(true){
						boolean f = true;
						if(k>=0){
							for(int j=q;j<q+p;j++){
								if(m[k][j])f = false;
							}
						}
						if(!f||k==-1){
							k++;
							for(int j=q;j<q+p;j++)m[k][j]=true;
							break;
						}
						k--;
					}
				}
				boolean con = true;
				int k = 0;
				while(k<5000&&con){
					con = false;
					boolean t = true;
					for(int j=0;j<5;j++){
						if(m[k][j])con = true;
						else t = false;
					}
					if(t){
						boolean f = true;
						int i = k;
						while(i<5000&&f){
							f = false;
							for(int j=0;j<5;j++){
								if(m[i][j])f = true;
							}
							if(f){
								for(int j=0;j<5;j++){
									m[i][j] = m[i+1][j];
								}
							}
							i++;
						}
					}
					else k++;
				}
//				p(m);
			}
			int s = 0;
			for(int i=0;i<5000;i++)for(int j=0;j<5;j++)s+=m[i][j]?1:0;
			System.out.println(s);
		}
	}
}