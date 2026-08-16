import java.util.Scanner;

public class Main {

	static int n;
	static boolean first;
	public static void main(String[] args) {
		Scanner cin=new Scanner(System.in);
		while(true){
			n=cin.nextInt();
			if(n==0)break;
			first=true;
			Page[] pages=new Page[n];
			for(int i=0;i<n;i++){
				pages[i]=new Page(cin.nextInt());
			}
			for(int i=1;i<n;i++){
				if(pages[i].num-1==pages[i-1].num){
					pages[i-1].next=pages[i];
					pages[i].prev=pages[i-1];
				}
			}
			for(int i=0;i<n;i++){
				if(pages[i].out()){
//					System.out.print(" ");
				}
			}
			System.out.println();
		}
	}
	static class Page{
		int num;
		Page next;
		Page prev;
		boolean already;
		Page(int a){
			num=a;
			already=false;
		}
		boolean out(){
			boolean re = false;
			if(already)return false;
			already=true;
			if(prev==null){
				if(first){
					first=false;
				}
				else{
					System.out.print(" ");
				}
				System.out.print(num);
				re=true;
			}
			if(next!=null){
				next.out();
			}
			else if(prev!=null){
				System.out.print("-"+num);
				re=true;
			}
			return re;
		}
	}
}