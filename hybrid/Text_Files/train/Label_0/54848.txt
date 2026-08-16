import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class Main {
	public static void main(String[] args)throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		while(true){
			String line[] = br.readLine().split(" ");
			int n = Integer.parseInt(line[0]);
			int k = Integer.parseInt(line[1]);
			if(n==0){break;}

			boolean dealt[] = new boolean[n+1];
			Arrays.fill(dealt, false);

			for(int i=0; i<k; i++){
				dealt[Integer.parseInt(br.readLine())] = true;
			}

			int count = 0;
			ArrayList<Integer> ladder = new ArrayList<Integer>();
			for(int i=1; i<=n; i++){
				if(dealt[i]){
					count++;
				}else{
					ladder.add(count);
					count = 0;
				}
			}
			ladder.add(count);

			int maxi = 0;
			if(dealt[0]){
				for(int i=0; i<ladder.size()-1; i++){
					int twosum = ladder.get(i).intValue() + ladder.get(i+1).intValue();
					if(twosum + 1 > maxi){maxi = twosum+1;}
				}
			}else{
				for(Integer cont:ladder){
					if(cont.intValue() > maxi){maxi = cont.intValue();}
				}
			}

			System.out.println(maxi);
		}
	}
}