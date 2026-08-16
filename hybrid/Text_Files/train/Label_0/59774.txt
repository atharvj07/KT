import java.util.Arrays;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;

public class Main{
	public static void main(String[] args){
		Scanner scan = new Scanner(System.in);
		ArrayList<String> str = new ArrayList<String>();
		while(scan.hasNext()){
			str.add(scan.nextLine());
		}
		Collections.sort(str);
		String be = "";
		int count = 0;
		String nt = "";
		for(int i = 0;i < str.size();i++){
			String[] ts = str.get(i).split(" ");
			if(ts[0].equals(be)){
				nt += " " + ts[1];
				count++;
				continue;
			}
			if(count > 1){
				String[] a = nt.split(" ");
				int[] b = new int[count];
				for(int j = 0;j < count;j++){
					b[j] = Integer.parseInt(a[j]);
				}
				Arrays.sort(b);
				for(int j = 0;j < count;j++){
					System.out.print(b[j]+((j == count-1)?"\n":" "));
				}
				count = 1;
				System.out.println(ts[0]);
				be = ts[0];
				nt = ts[1];
			}else{
				if(count != 0){
					System.out.println(nt);
				}
				System.out.println(ts[0]);
				be = ts[0];
				nt = ts[1];
				count = 1;
			}
		}
		if(count > 1){
			String[] a = nt.split(" ");
			int[] b = new int[count];
			for(int j = 0;j < count;j++){
				b[j] = Integer.parseInt(a[j]);
			}
			Arrays.sort(b);
			for(int j = 0;j < count;j++){
				System.out.print(b[j]+((j == count-1)?"\n":" "));
			}
		}else{
			System.out.println(nt);
		}
	}
}