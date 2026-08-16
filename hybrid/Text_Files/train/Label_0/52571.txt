import java.util.Scanner;
import java.util.ArrayList;
public class Main{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		ArrayList<Integer> list=new ArrayList<>();
		for(int i = 0; i<n; i++){
			list.add(sc.nextInt());
		}
		int[] ans=new int[n];
		for(int i = 0; i<n; i++){
			int ch=-1;
			for(int j=0; j<list.size(); j++){
				if(list.get(j)==j+1){
					ch=j;
				}
			}
			if(ch!=-1){
				ans[i]=list.remove(ch);
			}
			
		}
		if(list.size()>0){
			System.out.println(-1);
			return;
		}
		for(int i=n-1; i>=0; i--){
			System.out.println(ans[i]);
		}
	}
}
