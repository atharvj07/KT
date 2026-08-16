import java.util.*;
public class Main {
	final int INF = 1 << 24;
	
	private void doit(){
		Scanner sc = new Scanner(System.in);
		while(true){
			int n = sc.nextInt();
			int m = sc.nextInt();
			int c = sc.nextInt();
			int s = sc.nextInt();
			int g = sc.nextInt();
			if((n|m|c|s|g) == 0) break;
			s--;
			g--;
			int [][] mlist = new int[m][4];
			int [][][] dispass = new int [c][n][n];
			for(int i=0; i < c;i++){
				for(int j = 0; j < n; j++){
					Arrays.fill(dispass[i][j], INF);
					dispass[i][j][j] = 0;
				}
			}
			for(int i=0; i < m;i++){
				int from = sc.nextInt() -1;
				int to = sc.nextInt() - 1;
				int dis = sc.nextInt();
				int nowc = sc.nextInt() -1;
				mlist[i][0] = from;
				mlist[i][1] = to;
				mlist[i][2] = dis;
				mlist[i][3] = nowc;
				if(dispass[nowc][from][to] > dis){
					dispass[nowc][from][to] = dis;
					dispass[nowc][to][from] = dis;
				}
			}
			for(int cind = 0; cind < c; cind++){
				for(int j = 0; j < n; j++){
					for(int i = 0; i < n ; i++){
						for(int k = 0; k < n; k++){
							dispass[cind][i][k] = Math.min(dispass[cind][i][k], 
									dispass[cind][i][j] + dispass[cind][j][k]);
						}
					}
				}
			}
			
			int [] plist = new int[c];
			for(int i=0; i < c; i++){
				plist[i] = sc.nextInt();
			}
			ArrayList<ArrayList<Integer>> qlist = new ArrayList<ArrayList<Integer>>();
			ArrayList<ArrayList<Integer>> rlist = new ArrayList<ArrayList<Integer>>();
			for(int i=0; i < c; i++){
				qlist.add(new ArrayList<Integer>());
				qlist.get(i).add(0);
				rlist.add(new ArrayList<Integer>());
				for(int j = 0; j < plist[i] - 1; j++){
					qlist.get(i).add(sc.nextInt());
				}
				qlist.get(i).add(100000);
				for(int j = 0; j < plist[i]; j++){
					rlist.get(i).add(sc.nextInt());
				}
			}
			//create fare
			int [][] farelist = new int[c][100001];
			for(int cInd=0; cInd < c;cInd++){
				ArrayList<Integer> nowq = qlist.get(cInd);
				for(int i = 1; i < nowq.size();i++){
					for(int j = nowq.get(i-1) + 1 ; j <= nowq.get(i); j++){
						farelist[cInd][j] = farelist[cInd][j-1] + rlist.get(cInd).get(i-1);
					}
				}
			}
			
			//create pass
			int [][][] pass = new int[c][n][n];
			for(int i=0; i < c;i++){
				for(int j = 0; j< n; j++){
					Arrays.fill(pass[i][j], INF);
					pass[i][j][j] = 0;
				}
			}
			
			for(int cind = 0; cind < c; cind++){
				for(int j = 0; j < n; j++){
					for(int i = 0; i < n; i++){
						for(int k = 0; k < n; k++){
							int totaldis = dispass[cind][i][j] + dispass[cind][j][k];
							if(totaldis >= INF) continue;
							pass[cind][i][k] = Math.min(pass[cind][i][k], 
												farelist[cind][totaldis]);
						}
					}
				}
			}
			
			//All pass
			int [][] allPass = new int[n][n];
			for(int i=0; i < n;i++){
				Arrays.fill(allPass[i], INF);
				allPass[i][i] = 0;
			}
			for(int l = 0; l < c; l++){
				for(int j = 0; j < n; j++){
					for(int i = 0; i < n; i++){
						for(int k = 0; k < n;k++){
							int minij = INF, minjk = INF;
							//calc a minij, minjk
							for(int cind = 0; cind < c; cind++){
								minij = Math.min(minij, pass[cind][i][j]);
								minjk = Math.min(minjk, pass[cind][j][k]);
							}
							int value = Math.min(minij + minjk, allPass[i][j] + allPass[j][k]);
							allPass[i][k] = Math.min(allPass[i][k], value);
							//allPass[i][k] = Math.min(allPass[i][k], minij + minjk);
						}
					}
				}
			}
			int ans = allPass[s][g];
			if(ans >= INF){
				System.out.println(-1);
			}
			else{
				System.out.println(ans);
			}
		}
	}

	public static void main(String[] args) {
		Main obj = new Main();
		obj.doit();
	}
}