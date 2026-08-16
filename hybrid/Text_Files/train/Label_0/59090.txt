import java.util.*;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int t = sc.nextInt();
		
		String pre = "";
		int rst = 0;
		String[] s = new String[4];
		int[] u = new int[4];
		ArrayList<String> list = new ArrayList<String>();
		ArrayList<Integer> time = new ArrayList<Integer>();
		
		for(int i=0;i<n;i++){
			for(int j=0;j<4;j++) s[j] = sc.next();
			if(i!=0){
				u[0] = Integer.valueOf(s[0].substring(0, 2));
				u[1] = Integer.valueOf(s[0].substring(3, 5));
				u[2] = Integer.valueOf(pre.substring(0, 2));
				u[3] = Integer.valueOf(pre.substring(3, 5));
				rst = (u[1]-u[3]) + (u[0]-u[2])*60;
				if(rst>=t){
					list.add(s[1]);
					time.add(rst);
				}
			}
			pre = s[2];
		}
		
		System.out.println(list.size());
		for(int i=0;i<list.size();i++) System.out.println(list.get(i) + " " + time.get(i));
	}	
}