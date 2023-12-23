package pomTest;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.Assert;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;
import pageObjectModel.SauceCartPage;
import pageObjectModel.SauceCheckoutPage;
import pageObjectModel.SauceLoginPage;
import pageObjectModel.SauceProductPage;

import java.util.concurrent.TimeUnit;

public class SauceCartTest {
    WebDriver driver=null;

    @BeforeTest
    public void sauceTest() {
        System.setProperty("webdriver.chrome.driver", "C:\\Users\\odunuga\\kehinde-testify\\SeleniumWeb\\src\\chromedriver.exe");

        //Launch browser
        driver = new ChromeDriver();

        //Maximize the browser
        driver.manage().window().maximize();

        // Manage wait time
        driver.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);

        driver.get("https://www.saucedemo.com/");
    }
    // Navigate to saucedemo url
    @Test (priority = 0)
    public void navigateUrl(){
        driver.get("https://www.saucedemo.com/");
        System.out.println("Saucedemo url --- " + driver.getCurrentUrl());
    }

    @Test( groups = {"homePage"} )
     public void login() {
         SauceLoginPage login = new SauceLoginPage(driver);
         login.getUsername().sendKeys("standard_user");
         login.getPassword().sendKeys("secret_sauce");
         login.getLogin().click();
         System.out.println("---login successful");

         //verify user is the homepage
         String actualHomePage = driver.getCurrentUrl();
         WebElement menuIcon = driver.findElement(By.xpath("//button[@id='react-burger-menu-btn']"));

         if(menuIcon.isDisplayed()){
             System.out.println(actualHomePage + " you are on the HomePage");
         } else {
             System.out.println(actualHomePage + " you are not on the HomePage");
         }
     }

     @Test (priority = 2)
    public void products() throws InterruptedException {
        SauceProductPage products = new SauceProductPage(driver);
        products.getOnesie().click();
        products.getFleece().click();
        products.getBikeLight().click();
        Thread.sleep(3000);
         System.out.println("---products selected");
    }

    @Test (priority = 3)
     public void cart() throws InterruptedException {
        SauceCartPage cart = new SauceCartPage(driver);
        cart.getCart().click();
        Thread.sleep(3000);
        System.out.println("---cart");
    }
    @Test (priority = 4)
    public void verifyProducts(){
        // Assert that selected items are in cart
        SauceCartPage cart = new SauceCartPage(driver);
        String item1 = cart.getItem1().getText();
        String expectedItem1 = "Sauce Labs Onesie";
        String actualItem1 = item1;
        System.out.println("---"+ actualItem1 + " is added to cart");
        Assert.assertEquals(actualItem1, expectedItem1, "---Product is not in cart");

        String item2 = cart.getItem2().getText();
        String expectedItem2 = "Sauce Labs Bike Light";
        String actualItem2 = item2;
        System.out.println("---"+ actualItem2 + " is added to cart");
        Assert.assertEquals(actualItem2, expectedItem2, "---Product is not in cart");

        String item3 = cart.getItem3().getText();
        String expectedItem3 = "Sauce Labs Fleece Jacket";
        String actualItem3 = item3;
        System.out.println("---"+ actualItem3 + " is added to cart");
        Assert.assertEquals(actualItem3, expectedItem3, "---Product is not in cart");
    }

    @Test (priority = 5)
    public void checkOut() throws InterruptedException {
        SauceCheckoutPage checkOut = new SauceCheckoutPage(driver);
        checkOut.getCheckOut().click();
        Thread.sleep(3000);

        checkOut.getFirstname().sendKeys("Bolanle");
        checkOut.getLastname().sendKeys("Lawson");
        checkOut.getPostalCode().sendKeys("23401");
        Thread.sleep(3000);
        checkOut.getContinueBtn().click();
        System.out.println("---checkout successful");
        Thread.sleep(3000);
    }
    @Test (priority = 6)
    public void verifyCheckout() throws InterruptedException {
        // Assert that selected cart items are on checkout
        SauceCartPage cart = new SauceCartPage(driver);
        String item1 = cart.getItem1().getText();
        String expectedItem1 = "Sauce Labs Onesie";
        String actualItem1 = item1;
        System.out.println("---"+ actualItem1 + " is included in checkout");
        Assert.assertEquals(actualItem1, expectedItem1, "---Product is not in cart");

        String item2 = cart.getItem2().getText();
        String expectedItem2 = "Sauce Labs Bike Light";
        String actualItem2 = item2;
        System.out.println("---"+ actualItem2 + " is included in checkout");
        Assert.assertEquals(actualItem2, expectedItem2, "---Product is not in cart");

        String item3 = cart.getItem3().getText();
        String expectedItem3 = "Sauce Labs Fleece Jacket";
        String actualItem3 = item3;
        System.out.println("---"+ actualItem3 + " is included in checkout");
        Assert.assertEquals(actualItem3, expectedItem3, "---Product is not in cart");
        Thread.sleep(3000);
    }
    @Test (priority = 7)
    public void finishCheckout() throws InterruptedException {
        SauceCheckoutPage checkOut = new SauceCheckoutPage(driver);
        checkOut.getFinishBtn().click();
        Thread.sleep(3000);

        String successMessage = checkOut.getFinishPageHeader().getText();
        String expectedSuccessMessage = "Thank you for your order!";
        String actualSuccessMessage = successMessage;
        System.out.println(successMessage);
        Assert.assertEquals(actualSuccessMessage, expectedSuccessMessage, "---Success message is not correct");
        Thread.sleep(3000);
    }

    @AfterTest
    public void close(){
        driver.quit();
    }
}
