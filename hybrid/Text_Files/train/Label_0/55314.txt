import java.util.Scanner;
class Main{
 public static void main(String args[]){
Scanner sc=new Scanner(System.in);
int N= sc.nextInt();
int T= sc.nextInt();
int c[]=new int[N];
int t[]=new int[N];
for(int n=0;n<N;n++) {
c[n]=sc.nextInt();
t[n]=sc.nextInt();
 }
int cost=0;
boolean home=false;
for(int k=0;k<N;k++) {
	if(!home) {
	if(t[k]<=T) {
	cost=c[k];
	home=true;
	  }
	 }
 if(c[k]<cost) {
		if(t[k]<=T){
			cost=c[k];
		}
	}
}
System.out.println((home)?cost:"TLE");
 }
  }