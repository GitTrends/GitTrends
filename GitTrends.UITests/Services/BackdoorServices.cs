﻿using System;
using GitTrends.Mobile.Shared;
using Xamarin.UITest;
using Xamarin.UITest.Android;
using Xamarin.UITest.iOS;

namespace GitTrends.UITests
{
    static class BackdoorServices
    {
        public static void SetGitHubUser(IApp app, string accessToken) =>
            InvokeBackdoorMethod(app, BackdoorMethodConstants.SetGitHubUser, accessToken);

        public static object InvokeBackdoorMethod(this IApp app, string backdoorMethodName, string parameter = "") => app switch
        {
            iOSApp iosApp => iosApp.Invoke(backdoorMethodName + ":", parameter),
            AndroidApp androidApp when string.IsNullOrWhiteSpace(parameter) => androidApp.Invoke(backdoorMethodName),
            AndroidApp androidApp => androidApp.Invoke(backdoorMethodName, parameter),
            _ => throw new NotSupportedException("Platform Not Supported"),
        };
    }
}
