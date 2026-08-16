import java.io.*;

public class E implements Runnable{
	BufferedReader in;

	int n, m;	
	char[] a;
		
	int[] left, right, up, down;
	int[] l, r, u, d;
	
	int max, cnt, cur;
	
	void dfs(int ind){
		cur++;
		if (cur > max){max = cur; cnt = 1;} else
		if (cur== max)cnt++;
		
		if (l[ind] > -1) r[l[ind]] = r[ind];
		if (r[ind] > -1) l[r[ind]] = l[ind];
		if (u[ind] > -1) d[u[ind]] = d[ind];
		if (d[ind] > -1) u[d[ind]] = u[ind];
		
		switch(a[ind]){
		case 'L':
			if (l[ind] > -1) dfs(l[ind]);
			break;
		case 'R':
			if (r[ind] > -1) dfs(r[ind]);
			break;
		case 'U':
			if (u[ind] > -1) dfs(u[ind]);
			break;
		case 'D':
			if (d[ind] > -1) dfs(d[ind]);
			break;
		}

		if (l[ind] > -1) r[l[ind]] = ind;
		if (r[ind] > -1) l[r[ind]] = ind;
		if (u[ind] > -1) d[u[ind]] = ind;
		if (d[ind] > -1) u[d[ind]] = ind;		
		
		cur--;
	}
	
	@Override
	public void run() {
		try{
			in = new BufferedReader(new InputStreamReader(System.in));
			String[] temp = in.readLine().split(" ");
			n = Integer.parseInt(temp[0]);
			m = Integer.parseInt(temp[1]);
			
			a = new char[n * m];
			left = new int[n*m];
			right = new int[n*m];
			up = new int[n*m];
			down = new int[n*m];
			cnt = 0;
			
			for (int i=0; i<n; ++i){
				String str = in.readLine().trim();
				for (int j=0; j<m; ++j)
					a[cnt++] = (str.charAt(j));
			}
			
			// left & right
			for (int i=0; i<n; ++i){
				int last = -1;
				for (int j=0; j<m; ++j){
					left[i*m + j] = last;
					if (a[i*m + j] != '.') last = i * m + j;
				}
				last = -1;
				for (int j=m-1; j>=0; --j){
					right[i*m + j] = last;
					if (a[i*m + j] != '.') last = i * m + j;
				}
			}
			
			// up & down
			for (int j=0; j<m; ++j){
				int last = -1;
				for (int i=0; i<n; ++i){
					up[i*m + j] = last;
					if (a[i*m + j] != '.') last = i * m + j;
				}
				last = -1;
				for (int i=n-1; i>=0; --i){
					down[i*m + j] = last;
					if (a[i*m + j] != '.') last = i * m + j;
				}
			}
			
			max = 0; cnt = 0; cur = 0;
			
			for (int i=0; i<n*m; ++i)
				if (a[i] != '.'){
					l = left.clone();
					r = right.clone();
					u = up.clone();
					d = down.clone();
					cur = 0;
					//System.out.println(i);
					dfs(i);
				}
			
			System.out.println(max + " " + cnt);
		}catch(Exception ex){
				ex.printStackTrace();
			}
	}

	public static void main(String[] args) {
		(new Thread(new E())).start();
	}	

}
