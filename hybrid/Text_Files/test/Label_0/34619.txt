import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.Scanner;

public class Main{

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int k = sc.nextInt();
		int[] a = new int[n];
		int[] b = new int[n];
		for(int i =0 ;i<n;i++)
		{
			a[i] = sc.nextInt();
		}
		for(int i = 0;i<n;i++)
		{
			b[i] = sc.nextInt();
		}
		ArrayList<Idler> list = new ArrayList<Idler>();
		for(int i =0;i<n;i++)
		{
			Idler obj = new Idler();
			obj.setA(a[i]);
			obj.setT(b[i]);
			list.add(obj);
		}
		Collections.sort(list);
		HashSet<Integer> set = new HashSet<Integer>();
		ArrayList<Integer> lis = new ArrayList<Integer>();
		int count = 0;
		for (Idler idler : list) {
			if(set.contains(idler.getA()))
			{
				lis.add(idler.getT());
			}
			else{
				set.add(idler.getA());
				count++;
			}
		}
		Collections.sort(lis);
		int[] c = new int[lis.size()];
		int f = 0;
		for (Integer integer : lis) {
			c[f] = integer;
			f++;
		}
		long s = 0;
		for(int i = 0;i<k-count;i++)
		{
			s+=c[i];
		}
		System.out.println(s);
		sc.close();
	}

}
class Idler implements Comparable<Idler>{
	private int a;
	private int t;
	public int getA() {
		return a;
	}
	public void setA(int a) {
		this.a = a;
	}
	public int getT() {
		return t;
	}
	public void setT(int t) {
		this.t = t;
	}
	public int compareTo(Idler o) {
		return o.t-this.t;
	}
	
}
