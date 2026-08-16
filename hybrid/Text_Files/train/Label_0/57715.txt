import java.util.Scanner;
import java.util.ArrayList;
public class Main{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		double sum = 0;
		int answer = 0;
		double average = 0;
		double memo = 0;
		ArrayList<Double> arrayList = new ArrayList<Double>();
		for(int i = 0; i < a; i++){
			double b = sc.nextInt();
			sum += b;
			arrayList.add(b);
		}
		average = sum/a ;
		memo = arrayList.get(0);
		for(int i = 1; i < a; i++){
			if(Math.abs(average-memo)>Math.abs(average-arrayList.get(i))){
				memo = arrayList.get(i);
				answer = i;
			}
		}
		System.out.println(answer);
	}
}