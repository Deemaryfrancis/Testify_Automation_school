package Tasks;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.AfterClass;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

import java.util.concurrent.TimeUnit;

public class Task15 {
    WebDriver driver=null;

    @BeforeMethod
    public  void openBrowser(){
        System.setProperty("webdriver.chrome.driver", "C:\\Users\\odunuga\\kehinde-testify\\SeleniumWeb\\src\\chromedriver.exe");

        //Launch browser
        driver = new ChromeDriver();

        //Maximize the browser
        driver.manage().window().maximize();

        // Manage wait time
        driver.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);

        System.out.println("Browser launch------");
    }
    @Test
    public void googleTestify() throws InterruptedException {
        //Navigate to the url
        driver.get("https://www.google.com/");
        driver.findElement(By.name("q")).sendKeys("testify");
        Thread.sleep(3000);
        System.out.println("Google search Testify------");
        driver.close();
    }
    @Test
    public void mcDonalds() throws InterruptedException {
        //Navigate to the url
        driver.navigate().to("https://www.mcdonalds.com/us/en-us.html");
        Thread.sleep(3000);
        System.out.println("McDonalds orderNow button color------");
        String bgColor = driver.findElement(By.xpath("//a[@id='button-ordernow']")).getCssValue("background-color");
        System.out.println(bgColor);
    }
    @AfterMethod
    public void quitBrowser(){
        driver.close();
    }
}
