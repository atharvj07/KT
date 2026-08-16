import java.util.Scanner;

class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n=sc.nextInt();
		int team[] = new int [n];
		int a=0,b=0,as=0,bs=0;
		for(int i=0 ; i<n*(n-1)/2 ; i++){
			a=sc.nextInt();
			b=sc.nextInt();
			as=sc.nextInt();
			bs=sc.nextInt();
			if(as<bs){
				team[b-1]+=3;
			}else if(as>bs){
				team[a-1]+=3;
			}else{
				team[a-1]+=1;
				team[b-1]+=1;
			}
		}
		for(int i=0 ; i<n ; i++){
			int c=1;
			for(int j=0 ; j<n ; j++){
				if (team[i] < team[j]) {
                    c++;
                }
			}
			System.out.println(c);
		}
	}
}