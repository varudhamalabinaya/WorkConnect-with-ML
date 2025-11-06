/**
 * Frontend Validation Script for Freelancer Features
 * Run this in browser console on the Career Advisor page
 */

console.log("🚀 Starting Freelancer Features Validation...");

// Test 1: Check if Career Advisor page loads
function testPageLoad() {
    const header = document.querySelector('h1');
    if (header && header.textContent.includes('Grow and Earn AI')) {
        console.log("✅ Career Advisor page loaded successfully");
        return true;
    } else {
        console.log("❌ Career Advisor page not loaded properly");
        return false;
    }
}

// Test 2: Check if tabs are present and functional
function testTabsPresence() {
    const tabs = document.querySelectorAll('[role="tab"]');
    const expectedTabs = ['ML Insights', 'Market Trends'];
    
    if (tabs.length >= 2) {
        console.log("✅ Tabs are present on the page");
        
        // Check tab content
        tabs.forEach(tab => {
            const tabText = tab.textContent.trim();
            if (expectedTabs.some(expected => tabText.includes(expected))) {
                console.log(`✅ Found expected tab: ${tabText}`);
            }
        });
        return true;
    } else {
        console.log("❌ Expected tabs not found");
        return false;
    }
}

// Test 3: Check ML Insights content
function testMLInsights() {
    const mlContent = document.querySelector('[data-state="active"]');
    if (mlContent) {
        const projectRecs = mlContent.querySelector('h3');
        if (projectRecs && projectRecs.textContent.includes('Recommended Projects')) {
            console.log("✅ ML Insights content is displaying");
            
            // Check for recommendation cards
            const recCards = mlContent.querySelectorAll('.border.rounded-lg');
            console.log(`✅ Found ${recCards.length} recommendation cards`);
            return true;
        }
    }
    console.log("❌ ML Insights content not found or not displaying");
    return false;
}

// Test 4: Test Market Trends tab
function testMarketTrends() {
    return new Promise((resolve) => {
        const trendsTab = Array.from(document.querySelectorAll('[role="tab"]'))
            .find(tab => tab.textContent.includes('Market Trends'));
        
        if (trendsTab) {
            trendsTab.click();
            
            setTimeout(() => {
                const trendsContent = document.querySelector('[data-state="active"]');
                if (trendsContent) {
                    const trendItems = trendsContent.querySelectorAll('.border.rounded-lg');
                    if (trendItems.length > 0) {
                        console.log(`✅ Market Trends displaying ${trendItems.length} trend items`);
                        resolve(true);
                    } else {
                        console.log("❌ No trend items found in Market Trends");
                        resolve(false);
                    }
                } else {
                    console.log("❌ Market Trends content not accessible");
                    resolve(false);
                }
            }, 1000);
        } else {
            console.log("❌ Market Trends tab not found");
            resolve(false);
        }
    });
}

// Test 5: Check API connectivity
async function testAPIConnectivity() {
    try {
        // Test market trends API (no auth required)
        const response = await fetch('/api/market/trends?limit=5');
        if (response.ok) {
            const data = await response.json();
            console.log(`✅ Market Trends API working - ${data.trends?.length || 0} trends received`);
            return true;
        } else {
            console.log(`❌ Market Trends API failed - Status: ${response.status}`);
            return false;
        }
    } catch (error) {
        console.log(`❌ API connectivity error: ${error.message}`);
        return false;
    }
}

// Test 6: Check for JavaScript errors
function testJSErrors() {
    const errors = window.jsErrors || [];
    if (errors.length === 0) {
        console.log("✅ No JavaScript errors detected");
        return true;
    } else {
        console.log(`❌ ${errors.length} JavaScript errors detected:`, errors);
        return false;
    }
}

// Main validation function
async function runFreelancerValidation() {
    console.log("=" * 50);
    console.log("FREELANCER UI VALIDATION RESULTS");
    console.log("=" * 50);
    
    const results = [];
    
    // Run tests
    results.push({ test: "Page Load", passed: testPageLoad() });
    results.push({ test: "Tabs Presence", passed: testTabsPresence() });
    results.push({ test: "ML Insights", passed: testMLInsights() });
    results.push({ test: "Market Trends", passed: await testMarketTrends() });
    results.push({ test: "API Connectivity", passed: await testAPIConnectivity() });
    results.push({ test: "JS Errors", passed: testJSErrors() });
    
    // Summary
    const passed = results.filter(r => r.passed).length;
    const total = results.length;
    
    console.log(`\n📊 SUMMARY: ${passed}/${total} tests passed (${(passed/total*100).toFixed(1)}%)`);
    
    if (passed === total) {
        console.log("🎉 All freelancer features are working correctly!");
    } else {
        console.log("⚠️ Some issues detected. Check the logs above.");
    }
    
    return results;
}

// Error tracking
window.jsErrors = [];
window.addEventListener('error', (e) => {
    window.jsErrors.push({
        message: e.message,
        filename: e.filename,
        line: e.lineno
    });
});

// Auto-run validation
runFreelancerValidation();