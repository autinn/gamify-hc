# Performance Chart Visual Improvements and Data Updates

## At a high level, what changes were made?

This PR enhances the `PerformanceChart` component from a placeholder to a fully functional bar chart visualization with improved styling, dynamic label positioning, and hover tooltips. Additionally, it updates chart data formatting across `MainPage`, `CoursePage`, and `UnitPage` to use consistent labeling and realistic value ranges.

**Key changes:**
- Refactored `PerformanceChart` component with dynamic padding calculation and hover tooltips
- Improved chart styling with better label rotation and positioning
- Updated chart labels across all pages to use consistent "No. of questions answered" format
- Changed chart values from percentage-based (0-100) to count-based (0-20 questions)
- Added `labelOffset` prop support for customizable label positioning
- Improved unit labeling to show "Unit 1", "Unit 2", etc. based on `order_index`

## Why were these changes made?

1. **Better User Experience**: The previous chart was a placeholder with static styling that didn't adapt to different label lengths, causing overlap issues. The new implementation dynamically calculates padding based on label width.

2. **Visual Clarity**: Rotated labels were previously hardcoded and could overlap with bars or be cut off. The new dynamic positioning ensures labels are always visible and properly spaced.

3. **Data Consistency**: Chart labels and values were inconsistent across pages (some used percentages, some used different text). This PR standardizes them to show "No. of questions answered" with realistic count values (0-20).

4. **Improved Interactivity**: Added hover tooltips to show exact values when users hover over bars, making the chart more informative.

5. **Better Label Formatting**: Unit pages now display "Unit 1", "Unit 2" instead of full unit titles, which is cleaner and more consistent with the course structure.

## How were these changes made?

### PerformanceChart Component (`PerformanceChart.js` & `PerformanceChart.css`)

**JavaScript Changes:**
- Added `useState` and `useEffect` hooks to manage hover state and dynamic padding
- Implemented label width measurement using a hidden DOM element (`measureRef`)
- Added dynamic padding calculation: `Math.min(Math.max(maxLabelWidth + 30, 80), 150)` to prevent overlap while keeping reasonable bounds
- Added `labelOffset` prop (default: 50) to allow pages to customize label positioning
- Implemented hover tooltips that display the exact value when hovering over a bar
- Updated label positioning to use dynamic bottom offset: `bottom: -${dynamicPadding - labelOffset}px`

**CSS Changes:**
- Restructured CSS with clear section comments for maintainability
- Improved label rotation using `transform: rotate(-90deg) translateX(-50%)` with `transform-origin: left center`
- Added hover tooltip styling with arrow pointer
- Enhanced mobile responsiveness with adjusted spacing and font sizes
- Changed bar hover effect to trigger on wrapper hover for better UX
- Increased chart height from 180px to 200px for better visibility

### PageLayout Component

- Added `labelOffset` prop support to pass through to `PerformanceChart`
- Updated chart rendering to include the `labelOffset` prop

### Page Components (MainPage, CoursePage, UnitPage)

**MainPage.js:**
- Updated chart label from "Questions you answered correctly (% correct answered)" to "No. of questions answered"
- Changed values from hardcoded array `[65, 45, 55, 35]` to dynamic `courses.map(() => Math.floor(Math.random() * 21))`

**CoursePage.js:**
- Updated chart label to "No. of questions answered"
- Changed values from 0-100 range to 0-20 range
- Added unit sorting by `order_index` before generating chart data
- Updated labels to show "Unit 1", "Unit 2", etc. based on `order_index + 1` instead of full unit titles
- Passed sorted units to `UnitList` component

**UnitPage.js:**
- Updated chart label from "Problem Solving HCs" to "No. of questions answered"
- Changed values from 0-100 range to 0-20 range
- Added `labelOffset={70}` prop for better label spacing (concept names can be longer)
- Updated greeting to show "Course - Unit X" format using `order_index + 1`

## What context, visual or otherwise, do reviewers need to understand or use this feature?

### Visual Context

1. **Chart Appearance**: The chart now displays as a horizontal bar chart with:
   - Bars growing from bottom to top
   - Rotated labels (-90 degrees) below the x-axis
   - Hover tooltips appearing above bars on mouseover
   - Dynamic spacing that adapts to label length

2. **Label Positioning**: The `labelOffset` prop controls how far labels are positioned from the axis:
   - Default: 50px (used on MainPage and CoursePage)
   - UnitPage uses 70px for longer concept names
   - Higher values push labels further down, preventing overlap with axis labels

3. **Data Format**: All charts now consistently show:
   - X-axis labels: Course names, "Unit X", or concept names
   - Y-axis: Bar height represents count (0-20 questions)
   - Chart description: "No. of questions answered"

### Technical Context

- The dynamic padding calculation runs in a `useEffect` that measures each label's width using a hidden DOM element
- Padding is clamped between 80px (minimum) and 150px (maximum) to prevent extreme values
- The chart gracefully handles missing data with a placeholder message
- Mobile breakpoint at 768px adjusts spacing and font sizes

### Testing Context

Reviewers should test:
- Hovering over bars to see tooltips
- Charts with different label lengths (short course names vs. long concept names)
- Mobile viewport to ensure responsive design works
- Pages with no data to see placeholder message

## How Was the Code Tested?

### Manual Testing

1. **Visual Testing**:
   - Tested chart display on MainPage, CoursePage, and UnitPage
   - Verified labels don't overlap with bars or axis
   - Confirmed hover tooltips appear and display correct values
   - Tested with different label lengths (short course codes vs. longer concept names)

2. **Responsive Testing**:
   - Tested on mobile viewport (< 768px) to ensure spacing and font sizes adjust correctly
   - Verified bars and labels remain visible and properly positioned

3. **Data Testing**:
   - Verified chart displays correctly with empty data (shows placeholder)
   - Confirmed unit sorting works correctly on CoursePage
   - Tested "Unit X" label generation from `order_index`

4. **Cross-browser Testing**:
   - Tested in Chrome, Firefox, and Safari
   - Verified CSS transforms and positioning work consistently

### Code Review Checklist

- [x] Dynamic padding calculation handles edge cases (empty labels, very long labels)
- [x] Hover state management doesn't cause memory leaks
- [x] Label positioning formula is correct: `bottom: -${dynamicPadding - labelOffset}px`
- [x] Mobile styles don't break chart layout
- [x] All pages pass correct props to `PerformanceChart`

## Other Notes, Context, or Anything that Remains to be Addressed

### Known Limitations

1. **Random Data**: Chart values are currently generated using `Math.random()`. These should be replaced with real API data in a future PR when the backend provides progress/performance metrics.

2. **Value Range**: The 0-20 range is a placeholder. The actual range should be determined by real data once integrated.

3. **Tooltip Positioning**: Tooltips are positioned above bars but may overlap with other bars on narrow screens. Consider adding collision detection in the future if this becomes an issue.

### Future Improvements

1. **Real Data Integration**: Replace `Math.random()` values with actual API calls to fetch user progress data
2. **Animation**: Consider adding smooth transitions when chart data updates
3. **Accessibility**: Add ARIA labels and keyboard navigation support for screen readers
4. **Color Coding**: Consider using different colors for different performance ranges (e.g., green for high, yellow for medium, red for low)

### Dependencies

- No new dependencies added
- Uses existing React hooks (`useState`, `useEffect`, `useRef`)
- No changes to package.json

### Breaking Changes

- None. The `labelOffset` prop is optional with a sensible default, so existing code continues to work.

### Related Issues/PRs

- Part of the `style/progress-bar-visuals` branch
- Addresses visual improvements for performance charts across the application
