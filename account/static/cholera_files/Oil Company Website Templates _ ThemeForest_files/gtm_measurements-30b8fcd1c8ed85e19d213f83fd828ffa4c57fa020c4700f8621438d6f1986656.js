(()=>{var t={3806:t=>{t.exports={elementsDomain:"elements.envato.com",marketDomains:["themeforest.net","codecanyon.net","audiojungle.net","videohive.net","graphicriver.net","photodune.net","3docean.net","marketplace.envato.com","market.envato.com","envatomarketplaces.com","market.styleguide.envato.com"],tutsplusDomain:"tutsplus.com",skipNormalizationForAttributes:["elements_item_id"]}},6033:(t,e,a)=>{const n=a(3806),r=(t,e)=>e.some((e=>t.endsWith(e)));t.exports=(t,e={})=>{const a={...n,...e},i={};if(!t||!t.href)return i;const o=new URL(t.href,window.location.href);if(!["https:","http:"].includes(o.protocol))return i.eventName="external_click",i.linkUrl=o.toString(),i;const s=o.searchParams;return s.delete("_ga"),i.linkUrl=o.origin+o.pathname,i.linkDomain=o.host,i.linkQuery=s.toString(),i.linkAnchor=o.hash,i.eventName=((t,{elementsDomain:e,marketDomains:a,tutsplusDomain:n})=>{const i=window.location.host;return t.host===i?"internal_click":t.host.endsWith(e)?i.endsWith(e)?"internal_click":"elements_click":r(t.host,a)?r(i,a)?"internal_click":"market_click":"placeit.net"===t.host?"placeit_click":t.host.endsWith(n)&&i.endsWith(n)?"internal_click":"external_click"})(o,a),i}},8217:(t,e,a)=>{const{deepNormalizeAttributes:n,normalizeAttributeKey:r,normalizeAttributeValue:i}=a(2636),o=a(4383),s=a(8624),l=a(6033);t.exports={deepNormalizeAttributes:n,normalizeAttributeKey:r,normalizeAttributeValue:i,sendAnalyticsEvent:o,standardisedClickTracking:s,extractLinkAttributes:l}},2636:(t,e,a)=>{const n=a(3806),{isObject:r}=a(5633),i=(t,{stringifyArrays:e=!1,customConfig:a={}}={})=>{const l={...n,...a};if(Array.isArray(t))return e?s(t):t.map((t=>i(t,{stringifyArrays:e,customConfig:a})));if(r(t)){const n={};return Object.entries(t).forEach((([t,r])=>{const s=o(t);l.skipNormalizationForAttributes.includes(t)||l.skipNormalizationForAttributes.includes(s)?n[s]=r||void 0:n[s]=i(r,{stringifyArrays:e,customConfig:a})})),n}return s(t)},o=t=>t.replace(/\W+|\B(?=[A-Z])/g,"_").toLowerCase().replace(/[\s_]+/g,"_").replace(/^_+|_+$/g,""),s=t=>{if(void 0===t||null===t)return;let e;return Array.isArray(t)&&(e=e||t.map(s).filter(Boolean).join(", ")),e=e||t.toString().toLowerCase().trim().replace(/&amp;/g,"&").replace(/&#39;/g,"'").replace(/\s+/g," "),""!==e?e:void 0};t.exports={deepNormalizeAttributes:i,normalizeAttributeKey:o,normalizeAttributeValue:s}},4383:(t,e,a)=>{const{deepNormalizeAttributes:n}=a(2636),{isNonEmptyObject:r}=a(5633),i=t=>{window.dataLayer=window.dataLayer||[],window.dataLayer.push(t)},o=t=>{if(!t)return null;const e=setTimeout(t,500);return a=>{a?.startsWith("G-")&&(clearTimeout(e),t())}};t.exports=({eventName:t,eventType:e="user",callback:a=null,ecommerce:s=null,userAttributes:l=null,customConfig:c={},...u})=>{const d={event:"track_event",event_name:t,event_attributes:{event_type:e,custom_timestamp:Date.now(),...n(u,{stringifyArrays:!0,customConfig:c})},eventCallback:o(a)},m={event_attributes:null};r(l)&&(d.user_attributes=n(l,{stringifyArrays:!0,customConfig:c})),r(s)&&(d.event="e-commerce",d.ecommerce=n(s,{customConfig:c}),m.ecommerce=null),i(m),i(d)}},8624:(t,e,a)=>{const n=a(4383),r=a(3806),i=a(6033),o=t=>[t.dataset.analyticsClickLabel,t.textContent?.trim(),t.attributes.title?.value.trim(),t.attributes["aria-label"]?.value.trim(),t.attributes.alt?.value.trim()].find(Boolean),s=t=>{if(!t)return!1;if(t.closest('[data-analytics-has-custom-tracking="true"]'))return!1;if("A"===t.tagName){const e=t.attributes.href?.value.trim();return!!e&&!d(e)}return void 0!==t.dataset.analyticsClickLabel},l=[(u="#",t=>t===u),(c=/^javascript:/,t=>c.test(t))];var c,u;const d=t=>l.some((e=>e(t)));t.exports=(t,e={})=>{const a={...r,...e},l=[t.target,t.target.closest("a, [data-analytics-click-label]")].find(s);if(!l)return;const c=i(l,a),u={eventName:"internal_click",context:l.closest("[data-analytics-context]")?.dataset.analyticsContext,contextDetail:l.closest("[data-analytics-context-detail]")?.dataset.analyticsContextDetail,clickLabel:o(l),clickType:l.tagName,...c,customConfig:e};n(u)}},5633:t=>{const e=t=>"object"===typeof t&&"[object Object]"===Object.prototype.toString.call(t);t.exports={isObject:e,isNonEmptyObject:t=>e(t)&&Object.keys(t).length>0}}},e={};function a(n){var r=e[n];if(void 0!==r)return r.exports;var i=e[n]={exports:{}};return t[n](i,i.exports,a),i.exports}a.n=t=>{var e=t&&t.__esModule?()=>t.default:()=>t;return a.d(e,{a:e}),e},a.d=(t,e)=>{for(var n in e)a.o(e,n)&&!a.o(t,n)&&Object.defineProperty(t,n,{enumerable:!0,get:e[n]})},a.o=(t,e)=>Object.prototype.hasOwnProperty.call(t,e),(()=>{"use strict";var t,e=a(8217),n=a.n(e),r=function(t){if(!t.target.closest('[data-analytics-has-custom-click="true"]')){var e=t.target.closest("[data-analytics-click-payload]");if(e){var a,r,i,o,s,l,c,u=function(t){if(t)try{return JSON.parse(t)}catch(e){return void(document.body.dataset.railsEnv&&(window.Rollbar||console).error("MarketClickTracking error",e))}}(null===(a=e.dataset)||void 0===a?void 0:a.analyticsClickPayload);if(!u)return;null!==(r=u.context)&&void 0!==r||(u.context=null===(i=t.target.closest("[data-analytics-context]"))||void 0===i||null===(i=i.dataset)||void 0===i?void 0:i.analyticsContext),null!==(o=u.contextDetail)&&void 0!==o||(u.contextDetail=null===(s=t.target.closest("[data-analytics-context-detail]"))||void 0===s||null===(s=s.dataset)||void 0===s?void 0:s.analyticsContextDetail);var d,m=t.target.closest("a"),v=!("false"===(null===(l=t.target.closest("[data-turbo]"))||void 0===l||null===(l=l.dataset)||void 0===l?void 0:l.turbo))&&t.target.closest("[data-turbo-frame");if((null===m||void 0===m||null===(c=m.href)||void 0===c?void 0:c.startsWith("http"))&&!v)t.preventDefault(),null!==(d=u.callback)&&void 0!==d||(u.callback=function(){return window.open(m.href,m.target||"_self")});n().sendAnalyticsEvent(u)}else n().standardisedClickTracking(t)}};t=Symbol.for("marketClickTracking"),window[t]||(window[t]=r,window.addEventListener("click",window[t])),window.GtmMeasurements=n()})()})();
//# sourceMappingURL=/storefront/assets/gtm_measurements.js-34008b9b59ddb7d0be82a5eab86680e8fd6a225867a0b0f587dc5f54e5de25bb.map
//!
;
