import java.util.*;

public class Test
{
	private static int[][][][] electrons = new int[7][7][13][2];
	private static int count = 120;
	public static void main(String args[])
	{
		System.out.println("Electrons = "+count);
		int n = 1;
		int l = 0;
		for(int s = 1; s <9; s ++)
		{
			if(count <= 0)
				break;
			n = s/2 + 1;
			l = s - n;
			while(l > -1 && l < n)
			{
				fillOrbital(n, l);
				n ++;
				l --;
				if(count <= 0)
					break;
			}
			if(count <= 0)
				break;
		}
		for(int energyLevel = 1; energyLevel < 8; energyLevel ++)
		{
			System.out.println("Energy Level "+energyLevel);
			for(int suborbital = 0; suborbital < energyLevel; suborbital ++)
			{
				for(int m = -suborbital; m < suborbital + 1; m ++)
				{
					System.out.print(electrons[energyLevel - 1][suborbital][m+suborbital][0] + " ");
					System.out.print(electrons[energyLevel - 1][suborbital][m+suborbital][1] + "  ");
				}
				System.out.println();
			}	
		}
	}
	public static void fillOrbital(int n, int l)
	{
		System.out.println(count+" " +n+" "+ l);
		for(int m = -l; m < l + 1; m ++)
		{
			electrons[n-1][l][m+l][0] = 1;
			count --;
			if(count <= 0)
				break;
		}
		if(count <= 0)
			return;
		for(int m = -l; m < l + 1; m ++)
		{
			electrons[n-1][l][m+l][1] = -1;
			count --;
			if(count <= 0)
				break;
		}
	}
}