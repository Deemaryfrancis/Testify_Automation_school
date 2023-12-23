package Tasks;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.Assert;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

import java.util.concurrent.TimeUnit;

public class Task16 {
    WebDriver driver=null;

    @BeforeClass
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
    public void testify() throws InterruptedException {
        //Navigate to the url
        driver.get("https://testifyltd.com/");
        driver.findElement(By.xpath("//a[contains(text(),'Contact Us')]")).click();
        Thread.sleep(3000);
    }
    @Test
    public  void email() throws InterruptedException {
        WebElement emailT = driver.findElement(By.xpath("//span[contains(text(),'info@testifyltd.com')]"));
        Thread.sleep(3000);
        System.out.println(emailT.getText());
        String email = emailT.getText();
        Assert.assertEquals(email, "info@testifyltd.com");
    }
    @Test
    public  void location() throws InterruptedException {
        WebElement locationT = driver.findElement(By.xpath("//span[contains(text(),'Nigeria')]"));
        Thread.sleep(3000);
        System.out.println(locationT.getText());
        String location = locationT.getText();
        Assert.assertEquals(location, "Nigeria");
    }
    @Test
    public  void phone() throws InterruptedException {
        WebElement phoneT = driver.findElement(By.xpath("//span[contains(text(),'(+234)905-882-0971')]"));
        Thread.sleep(3000);
        System.out.println(phoneT.getText());
        String phone = phoneT.getText();
        Assert.assertEquals(phone, "(+234)905-882-0971");
    }
    @AfterClass
    public void closeBrowser(){
        driver.quit();
    }
}
