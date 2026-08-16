import java.io.*;
import java.util.*;
import static java.lang.Math.*;
import java.math.BigInteger;
public class Main{
	public static void main(String[] args){
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		int y = n/3 - 1;
		int x = n/3 + 2;
		for(int i=y; i<=x; i++){
			for(int j=i; j<=x; j++){
				for(int k=j; k<=x; k++){
					if(i+j+k == n && i%3!=0 && j%3!=0 && k%3!=0){
						System.out.println(i+" "+j+" "+k);
						return;
					}
				}
			}
		}
	}
}	