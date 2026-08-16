import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.*;
import java.util.*;

public class t1{
	public static void main(String[] args) {
		Scanner scan=new Scanner(System.in);
		int n=scan.nextInt();
		String[] ary=new String[n];
		scan.nextLine();
		for(int i=0;i<n;i++){
			ary[i]=scan.nextLine();
			
		}
		int sum=0;
		for(int i=0;i<n;i++){
			switch(ary[i]){
				case "Tetrahedron":
					sum=sum+4;
					break;
				case "Cube":
					sum=sum+6;
					break;	
				case "Octahedron":
					sum=sum+8;
					break;	
				case "Dodecahedron":
					sum=sum+12;
					break;	
				case "Icosahedron":
					sum=sum+20;
					break;
				default:
					sum=sum;					
			}	
		}
		
		System.out.println(sum);
		
	}
	
	

}
	


