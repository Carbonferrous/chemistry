import java.util.*;

public class Test
{
	public static void main(String args[])
	{
		Atom A = new Atom(79);
		A.fillElectrons(1);
		for(int[] e:A.getElectrons())
		{
			for(int x:e)
			{
				System.out.print(x + " ");
			}
			System.out.println();
		}
		
	}
}