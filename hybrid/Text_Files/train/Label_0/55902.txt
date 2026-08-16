import java.util.Scanner;
import java.util.HashMap;
import java.util.Arrays;
class Main
{
	public static void main(String args[])
	{
		Scanner sc = new Scanner(System.in).useDelimiter("[\n#]+");
		while (true)
		{
			String str = sc.next();
			if (str.equals("0")) break;
			int rk = Integer.parseInt(str.substring(0, 2), 16);
			int gk = Integer.parseInt(str.substring(2, 4), 16);
			int bk = Integer.parseInt(str.substring(4, 6), 16);
			int d[] = new int[8];
			HashMap<Integer, String> map = new HashMap<Integer, String>();
			d[0] = (0x00 - rk) * (0x00 - rk)
					+ (0x00 - gk) * (0x00 - gk)
					+ (0x00 - bk) * (0x00 - bk);
			map.put(d[0], "black");
			d[1] = (0x00 - rk) * (0x00 - rk)
					+ (0x00 - gk) * (0x00 - gk)
					+ (0xff - bk) * (0xff - bk);
			map.put(d[1], "blue");
			d[2] = (0x00 - rk) * (0x00 - rk)
					+ (0xff - gk) * (0xff - gk)
					+ (0x00 - bk) * (0x00 - bk);
			map.put(d[2], "lime");
			d[3] = (0x00 - rk) * (0x00 - rk)
					+ (0xff - gk) * (0xff - gk)
					+ (0xff - bk) * (0xff - bk);
			map.put(d[3], "aqua");
			d[4] = (0xff - rk) * (0xff - rk)
					+ (0x00 - gk) * (0x00 - gk)
					+ (0x00 - bk) * (0x00 - bk);
			map.put(d[4], "red");
			d[5] = (0xff - rk) * (0xff - rk)
					+ (0x00 - gk) * (0x00 - gk)
					+ (0xff - bk) * (0xff - bk);
			map.put(d[5], "fuchsia");
			d[6] = (0xff - rk) * (0xff - rk)
					+ (0xff - gk) * (0xff - gk)
					+ (0x00 - bk) * (0x00 - bk);
			map.put(d[6], "yellow");
			d[7] = (0xff - rk) * (0xff - rk)
					+ (0xff - gk) * (0xff - gk)
					+ (0xff - bk) * (0xff - bk);
			map.put(d[7], "white");
			Arrays.sort(d);
			System.out.println(map.get(d[0]));
		}
	}
}