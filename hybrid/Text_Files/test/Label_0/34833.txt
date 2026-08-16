import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Radio_Station {
	public static void main(String[] args)throws Throwable {
		BufferedReader bf=new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st=new StringTokenizer(bf.readLine());
		int servers=Integer.parseInt(st.nextToken());
		int commands=Integer.parseInt(st.nextToken());
		HashMap<String, String> map=new HashMap<String,String>();
		while(servers-->0)
		{
			st=new StringTokenizer(bf.readLine());
			String a=st.nextToken();
			String b=st.nextToken()+";";
			map.put(b, a);
		}
		while(commands-->0)
		{
			st=new StringTokenizer(bf.readLine());
			System.out.print(st.nextToken()+" ");
			String a=st.nextToken();
			System.out.println(a+" #"+map.get(a));
		}
	}
}
