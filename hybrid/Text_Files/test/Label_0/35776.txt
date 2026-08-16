import java.io.*;
import java.util.*;

public class cellularnetwork {
    
    public static TreeSet<Integer> towers;
    public static Set<Integer> cities;
    
	public static void main (String [] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		towers = new TreeSet<>();
        cities = new HashSet<>();
        
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            cities.add(Integer.parseInt(st.nextToken()));
        }
        
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            towers.add(Integer.parseInt(st.nextToken()));
        }
		
//        System.out.println(towers + " " + cities);
        
        int maxDist = Integer.MIN_VALUE;
        for (int city : cities) {
            Integer lowerCity = towers.floor(city);
            Integer higherCity = towers.ceiling(city);
            int curMin = Integer.MAX_VALUE;
            if (lowerCity != null) {
                curMin = Math.min(curMin, city - lowerCity);
            }
            if (higherCity != null) {
                curMin = Math.min(curMin, higherCity - city);
            }
            
            maxDist = Math.max(maxDist, curMin);
        }
        
		PrintWriter pw = new PrintWriter(System.out);
		pw.println(maxDist);
		pw.close();
	}	
}