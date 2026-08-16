import java.util.Scanner;

    public class Main{
        public void solve(){
		int n,k,zero,ichi;
		ichi = 0;
		zero = 0;
        Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		while(n!=0){
			for(int i=0;i<n;i++){
				k = sc.nextInt();
				if(k<=1){
					ichi++;
				}
				if(k<=0){
					zero++;
				}
			}
			if(n==ichi){
				System.out.println("NA");
			}else{
				System.out.println(n-zero+1);
			}
			n=sc.nextInt();
			ichi = 0;
			zero = 0;
		}
        }
    public static void main(String[]args){
    Main obj = new Main();
    obj.solve();
    }
    }