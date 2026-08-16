import java.util.*;
public class MexicanWave {

	void solve()
	{
		Scanner in = new Scanner(System.in);
		long ax = in.nextLong();
        long ay = in.nextLong();
        long bx = in.nextLong();
        long by = in.nextLong();
        long cx = in.nextLong();
        long cy = in.nextLong();

        if ((ax * (by - cy) + (bx * (cy - ay)) + (cx * (ay - by))) == 0) {
            System.out.println("No");
            return;
        }

        long value1 = (bx - ax) * (bx - ax) + ((by - ay) * (by - ay));
        long value2 = (bx - cx) * (bx - cx) + ((by - cy) * (by - cy));

        if (value1 == value2)
            System.out.println("Yes");
        else
            System.out.println("No");
			
	}
	
	
	public static void main(String[] args) {
		new MexicanWave().solve();

	}

}
