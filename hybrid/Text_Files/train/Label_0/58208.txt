import java.util.*;

public class CF
{
	public static void main(String[] args)
	{
        Scanner scan = new Scanner(System.in);
char[] r = scan.next().toCharArray();
boolean good = true;
char curr = 'a';
for (int a = 0; a < r.length; a++)
{
if (curr == r[a])
curr++;
else if (curr < r[a])
good = false;
}
		System.out.println(good ? "YES" : "No");
	}
}