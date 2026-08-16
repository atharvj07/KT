import java.util.Scanner;
public class Main{
	public static void main(String[] args){
		Scanner scan = new Scanner(System.in);
        while(scan.hasNext()){
        	int n = scan.nextInt();
        	int s = scan.nextInt();
        	if(n == 0 && s == 0){
        		break;
        	}
        	int[] r = new int[n];
        	for(int i = 0;i < n;i++){
        		r[i] = scan.nextInt();
        	}
        	int count = 0;
        	for(int i = 0;i < n-1;i++){
        		for(int j = i + 1;j < n;j++){
        			if(r[i]+r[j] > s){
        				count++;
        			}
        		}
        	}
        	System.out.println(count);
        }
	}
}