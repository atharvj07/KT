import java.util.Scanner;

public class Problem {
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        while(t-->0) {
        	int n=sc.nextInt();
        	int a[]=new int[n];
        	for(int i=0;i<n;i++) {
        		a[i]=sc.nextInt();
        	}
        	int even=0,odd=0,index=0;
        	int wrongEvens=0;
        	for(int i=0;i<n;i++) {
        		if(a[i]%2==0) {
        			even++;
        		}
        		else {
        			odd++;
        			if(i%2==0) {
        				wrongEvens++;
        			}
        		}
        		index++;
        	}
        	int evenSpots=(n+1)/2,oddSpots=n/2;
        	if(evenSpots!=even||oddSpots!=odd) {
        		System.out.println(-1);
        	}
        	else {
        		System.out.println(wrongEvens);
        	}
        }
		}
	}

