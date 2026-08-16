import java.util.Arrays; 
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		while(true){
			final int n = sc.nextInt();
			final int m = sc.nextInt();
			
			if(n == 0 && m == 0){
				break;
			}
			
			boolean[] is_legal = new boolean[n];
			String[] source_pattern = new String[n];
			String[] destination_pattern = new String[n];
			
			for(int i = 0; i < n; i++){
				final String act = sc.next();
				final String so = sc.next();
				final String de = sc.next();
				
				is_legal[i] = "permit".equals(act);
				source_pattern[i] = so.replaceAll("\\?", ".");
				destination_pattern[i] = de.replaceAll("\\?", ".");
				
				//System.out.println(is_legal[i] + " => " + source_pattern[i] + " : " + destination_pattern[i]);
			}
			
			LinkedList<String> list = new LinkedList<String>();
			
			for(int i = 0; i < m; i++){
				boolean ok = false;
				
				String from = sc.next();
				String to = sc.next();
				String mes = sc.next();
				
				for(int j = n - 1; j >= 0; j--){
					if(from.matches(source_pattern[j]) && to.matches(destination_pattern[j])){
						if(is_legal[j]){
							ok = true;
						}else{
							ok = false;
						}
						
						break;
					}
				}
				
				if(!ok){
					continue;
				}
				
				list.add(from + " " + to + " " + mes);
			}
			
			System.out.println(list.size());
			
			for(String str : list){
				System.out.println(str);
			}
			
		}
		
		sc.close();
	}
}