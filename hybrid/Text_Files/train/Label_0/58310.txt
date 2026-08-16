import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;



public class Solution {
    public static void main(String[] args)  {
       	Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		int t = scan.nextInt();
		int ans = 0;
		ArrayList<Integer> list = new ArrayList();
		for (int i = 0; i < n; i++){
			int center = scan.nextInt()*2;
			int storona = scan.nextInt();
			list.add(center-storona);
			list.add(center+storona);
		}
		Collections.sort(list);
		for (int i = 1; i < n*2 - 1 ; i+=2){
			if (list.get(i+1)-list.get(i)>t*2){
				ans+=2;
			}
			else if (list.get(i+1)-list.get(i)==t*2){
			   ans+=1;
			}
			
		}
		System.out.println(ans+2);
    }
}