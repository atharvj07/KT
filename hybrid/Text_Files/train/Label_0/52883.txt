import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Scanner;

// Java8
public class Main
{
	Scanner sc = new Scanner(System.in);

	public static void main(String[] args) throws Exception
	{
		new Main().run();
	}

	void run()
	{
		int n = nint();
		int[] ds = new int[n];
		for(int i=0; i<n; i++) ds[i] = nint();

		System.out.println(judge(n, ds) ? "yes" : "no");
	}

	boolean judge(int n, int[] ds)
	{
		PriorityQueue<Integer> minHeap = new PriorityQueue<>(n, Comparator.naturalOrder());
		minHeap.offer(ds[0]);
		for(int i=1; i<n; i++)
		{
			while(!minHeap.isEmpty())
			{
				int x = minHeap.peek();
				if(x<i*10) minHeap.poll();
				else break;
			}
			if(minHeap.isEmpty()) return false;
			minHeap.offer(i*10+ds[i]);
		}
		PriorityQueue<Integer> maxHeap = new PriorityQueue<>(n, Comparator.reverseOrder());
		maxHeap.offer((n-1)*10-ds[n-1]);
		for(int i=n-2; i>=0; i--)
		{
			while(!maxHeap.isEmpty())
			{
				int x = maxHeap.peek();
				if(x>i*10) maxHeap.poll();
				else break;
			}
			if(maxHeap.isEmpty()) return false;
			maxHeap.offer(i*10-ds[i]);
		}
		return true;
	}

	int nint()
	{
		return Integer.parseInt(sc.next());
	}
}
