import java.util.Arrays;
import java.util.Scanner;

//Magic Slayer
public class Main{

	void run(){
		int INF = 1<<29;
		Scanner sc = new Scanner(System.in);
		for(;;){
			int n = sc.nextInt();
			if(n==0)break;
			int[] hp = new int[n];
			for(int i=0;i<n;i++)hp[i]=sc.nextInt();
			Arrays.sort(hp);
			int maxhp = hp[n-1];
			int m = sc.nextInt();
			int sn = 0, an = 0;
			int[] singleD = new int[m];
			int[] singleM = new int[m];
			int[] allD = new int[m];
			int[] allM = new int[m];
			for(int i=0;i<m;i++){
				sc.next();
				int mp = sc.nextInt();
				boolean f = "Single".equals(sc.next());
				int d = sc.nextInt();
				if(d==0)continue;
				if(f){
					singleD[sn] = d;
					singleM[sn] = mp;
					sn++;
				}
				else{
					allD[an] = d;
					allM[an] = mp;
					an++;
				}
			}
			int[] sdp = new int[maxhp+1];
			Arrays.fill(sdp, INF);
			sdp[0] = 0;
			if(sn>0){
				for(int d=1;d<=maxhp;d++)sdp[d] = ((d-1)/singleD[0]+1)*singleM[0];
				for(int i=1;i<sn;i++){
					for(int d=1;d<=maxhp;d++){
						if(d-singleD[i]<=0)sdp[d] = Math.min(sdp[d], singleM[i]);
						else sdp[d] = Math.min(sdp[d], sdp[d-singleD[i]]+singleM[i]);
					}
				}
			}
			int[] adp = new int[maxhp+1];
			Arrays.fill(adp, INF);
			adp[0] = 0;
			if(an>0){
				for(int d=1;d<=maxhp;d++)adp[d] = ((d-1)/allD[0]+1)*allM[0];
				for(int i=1;i<an;i++){
					for(int d=1;d<=maxhp;d++){
						if(d-allD[i]<=0)adp[d] = Math.min(adp[d], allM[i]);
						else adp[d] = Math.min(adp[d], adp[d-allD[i]]+allM[i]);
					}
				}
			}
//			debug(sdp);
//			debug(adp);
			int min = INF;
			for(int d=0;d<=maxhp;d++){
				int mp = adp[d];
				for(int i=0;i<n;i++){
					mp += sdp[Math.max(0, hp[i]-d)];
					if(INF<=mp){
						mp = INF;
						break;
					}
				}
				min = Math.min(min, mp);
			}
			System.out.println(min);
		}
	}
	
	void debug(Object...o){
		System.out.println(Arrays.deepToString(o));
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}