import java.util.*;

public class Main{
	//2338 start
	
	int [] p1 = {0,0,1,1,2,2};
	int [] p2 = {1,2,0,2,0,1};
	int [] p3 = {2,1,2,0,1,0};
	
	private void doit(){
		Scanner sc = new Scanner(System.in);
		while(true){
			int n = sc.nextInt();
			if(n == 0) break;
			int [][] data = new int[n][3];
			for(int i = 0; i < n; i++){
				for(int j = 0; j < 3; j++){
					data[i][j] = sc.nextInt();
				}
			}
			
			ArrayList<ArrayList<Integer>> list = new ArrayList<ArrayList<Integer>>();
			for(int i = 0; i < n; i++){
				list.add(new ArrayList<Integer>());
				
				for(int j = 0; j < 6; j++){
					int h = data[i][p1[j]];
					int m = data[i][p2[j]];
					int s = data[i][p3[j]];
					
					
					for(int offset = 0; offset < 60; offset++){
						int hh = (h + offset) % 60;
						int mm = (m + offset) % 60;
						int ss = (s + offset) % 60;
						if(hh % 5 != mm / 12) continue;
						list.get(i).add(calc(hh / 5, mm, ss));
						//System.out.println(hh + " " + mm + " " + ss + " " + calc(hh % 12, mm, ss));
					}
				}
				Collections.sort(list.get(i));
				//System.out.println(list.get(i));
			}
			
			int INF = 1 << 24;
			int anss = INF, anse = 0, diff = INF;
			for(int i = 0; i < n; i++){
				for(int j = 0; j < list.get(i).size(); j++){
					int s = list.get(i).get(j);
					int e = s;
					boolean flg = true;
					for(int k = 0; k < n; k++){
						if(i == k) continue;
						int ke = -1;
						for(int kk = 0; kk < list.get(k).size(); kk++){
							int temp = list.get(k).get(kk);
							if(temp >= s){
								ke = temp;
								break;
							}
						}
						if(ke == -1){
							flg = false;
							break;
						}
						e = Math.max(e, ke);
					}
					if(! flg) continue;
					int d = e - s;
					if(d < diff){
						anss = s;
						anse = e;
						diff = d;
					}
					else if(d == diff && s < anss){
						anss = s;
						anse = e;
					}
				}
			}
			//System.out.println(anss + " " + anse + "diff = " + diff);
			print(anss, anse);
		}
	}
	
	private int [] totime(int time){
		int h = time / 3600;
		int m = (time - 3600 * h) / 60;
		int s = time - 3600 * h - 60 * m;
		return new int[]{h,m,s};
	}

	private void print(int anss, int anse) {
		int [] s = totime(anss);
		int [] e = totime(anse);
		System.out.printf("%02d:%02d:%02d ",s[0], s[1], s[2]);
		System.out.printf("%02d:%02d:%02d\n", e[0], e[1], e[2]);
	}

	private int calc(int hh, int mm, int ss) {
		return hh * 3600 + mm * 60 + ss;
	}

	public static void main(String[] args) {
		new Main().doit();
	}
}