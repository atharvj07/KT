import java.util.HashMap;
import java.util.Scanner;

public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		HashMap<Integer,Integer> hash = new HashMap<Integer,Integer>();
		for(int i=0;i<n;i++){
			int a = sc.nextInt();
			Integer po = hash.get(a);
			if(po  == null){
				po = 0;
			}
			hash.put(a, po+1);	
		}
		int ans = 0;
		for(int i:hash.keySet()){
			Integer po = hash.get(i);
			if(po == null){
				continue;
			}else{
				if(po >= i){
					ans = ans + (po - i);
				}else{
					ans = ans + po;
				}
			}
		}
		System.out.println(ans);
	}
}
