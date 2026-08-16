import java.util.*;

public class Main{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		while(true){
			int n = sc.nextInt();
			if(n == 0) break;

			ArrayList<HashSet<Integer>> set = new ArrayList<HashSet<Integer>>();
			boolean[][] flg = new boolean[n][32];

			for(int i=0;i<n;i++){
				set.add(new HashSet<Integer>());
				set.get(i).add(i);

				int m = sc.nextInt();

				for(int j=0;j<m;j++){
					int x = sc.nextInt();
					flg[i][x-1] = true;
				}
			}

			int ans = 0;
			for(;ans<30;ans++){
				HashSet<Integer> tmp = new HashSet<Integer>();
				for(int j=0;j<n;j++){
					if(flg[j][ans]){
						tmp.addAll(set.get(j));
					}
				}
				if(tmp.size() == n) break;

				for(int j=0;j<n;j++){
					if(flg[j][ans]){
						set.get(j).addAll(tmp);
					}
				}
			}

			System.out.println(ans==30 ? -1 : ans+1);
		}
	}
}